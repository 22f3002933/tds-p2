from fastapi import FastAPI, Query, HTTPException, Form, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated, Dict, Optional, List, Any, Tuple
from pathlib import Path

from questions.question_template import question_templates

import uvicorn
import tempfile
import os
import pickle
import httpx
import re
import numpy as np
import json
import base64
import mimetypes

from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Enable CORS to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

EMBEDDINGS_CACHE_FILE = "question_embeddings_cache.pkl"

# function to generate embeddings using OpenAI API
def custom_openai_embedding_function(texts: List[str]) -> List[List[float]]:
    """Generate embeddings using OpenAI API with httpx"""
    # Check if texts is a single string and convert to list if needed
    if isinstance(texts, str):
        texts = [texts]
    
    # Ensure all items are strings
    texts = [str(text).strip() for text in texts if text]
    
    api_key = os.getenv('AIPROXY_TOKEN')
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    data = {
        "input": texts,
        "model": "text-embedding-3-small"
    }
    
    # Using httpx instead of requests
    with httpx.Client(timeout=30.0) as client:
        response = client.post(
            "http://aiproxy.sanand.workers.dev/openai/v1/embeddings",
            headers=headers,
            json=data
        )
    
    if response.status_code == 200:
        embeddings = [item['embedding'] for item in response.json()['data']]
        return embeddings
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")

# load or create embeddings for the question templates
def load_or_create_embeddings(question_templates: Dict[str, str], force_refresh: bool = False) -> Dict[str, List[float]]:
    """Load embeddings from cache or generate new ones if needed"""
    question_embeddings = {}
    cache_file = Path(EMBEDDINGS_CACHE_FILE)
    
    # Try to load from cache if it exists and we're not forcing a refresh
    if cache_file.exists() and not force_refresh:
        try:
            with open(cache_file, 'rb') as f:
                cached_data = pickle.load(f)
                
            # Check if all templates are in the cache
            all_templates_cached = all(q_id in cached_data for q_id in question_templates)
            
            if all_templates_cached:
                print("Loaded embeddings from cache file")
                return cached_data
            else:
                print("Cache exists but doesn't contain all templates, regenerating...")
        except Exception as e:
            print(f"Error loading cache: {e}, regenerating...")
    
    # Generate embeddings for all templates
    print("Generating embeddings for question templates...")
    template_texts = []
    template_ids = []
    
    for q_id, q_statement in question_templates.items():
        clean_template = re.sub(r'\{\w+\}', "X", q_statement)
        template_texts.append(clean_template)
        template_ids.append(q_id)
    
    # Get embeddings in a single API call for efficiency
    embeddings = custom_openai_embedding_function(template_texts)
    
    # Map embeddings back to question IDs
    for i, q_id in enumerate(template_ids):
        question_embeddings[q_id] = embeddings[i]
    
    # Save to cache file
    with open(cache_file, 'wb') as f:
        pickle.dump(question_embeddings, f)
    print(f"Saved {len(question_embeddings)} embeddings to cache file")
    
    return question_embeddings

# identify the question id from the question statement using cache file
def identify_question_with_file_cache(problem_statement: str, question_embeddings: Dict[str, List[float]]) -> Tuple[Optional[str], float]:
    """Identify the most similar question template using file-cached embeddings"""
    # Replace numbers with X to focus on the structure of the question
    normalized_statement = re.sub(r'\b\d+(\.\d+)?\b', 'X', problem_statement)
    
    # Generate embedding for the input problem statement
    input_embedding = custom_openai_embedding_function(normalized_statement)[0]
    
    # Find the most similar question template
    max_similarity = -1
    best_match_id = None
    
    for q_id, q_embedding in question_embeddings.items():
        # Calculate cosine similarity
        similarity = np.dot(input_embedding, q_embedding) / (np.linalg.norm(input_embedding) * np.linalg.norm(q_embedding))
        
        if similarity > max_similarity:
            max_similarity = similarity
            best_match_id = q_id
    
    return best_match_id, max_similarity

# identify the question id from the question statement
def identify_question(problem_statement: str, question_templates: Dict[str, str], force_refresh: bool = False) -> Tuple[Optional[str], float]:
    question_embeddings = load_or_create_embeddings(question_templates, force_refresh)
    return identify_question_with_file_cache(problem_statement, question_embeddings)


# the function is present with the function name in ./answers/functions/ques_name.py 
async def eval (func_name: str, ques_id: str):
    module = __import__(f"answers.functions.{ques_id}", fromlist=[func_name])
    func = getattr(module, func_name)
    print(func_name)
    func_result = func()
    return func_result

# gets the answers from answers.json for the matched quesId
# 1. direct answer -> string, int, float, json object
# 2. function call -> function:name
# 3. file as a response -> file:file_path ( returns a base64 encoded file )
async def solver(match_ques_id: str):
    with open("./answers/answers.json", "r") as f:
        answers = json.load(f)

    answer = answers[match_ques_id]

    if isinstance(answer, str) and answer.startswith("function:"):
        func_name = answer.split(":")[1]
        answer = await eval(func_name, ques_id=match_ques_id)
        # answer
    elif isinstance(answer, str) and answer.startswith("file:"):
        file_name = answer.split(":")[1]
        file_path = os.path.join("./answers/files/", file_name)
        # ensure the answer is base64 encoded file
        with open(file_path, "rb") as f:
            answer = base64.b64encode(f.read()).decode("utf-8")
            mime_type, _ = mimetypes.guess_type(file_path)
            mime_type = mime_type or "application/octet-stream"

            answer = f"data:{mime_type};base64,{answer}"

    return answer

@app.post("/api")
async def api(question: Annotated[str, Form()], file: UploadFile | None = None):
    if file:
        temp_dir = tempfile.mkdtemp()
        file_path = os.path.join(temp_dir, file.filename)
        
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        
    matched_ques_id, similarity = identify_question(question, question_templates)
    print(matched_ques_id, similarity)

    answer  = await solver(matched_ques_id)
    print(answer)

    return { "answer": answer }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)
