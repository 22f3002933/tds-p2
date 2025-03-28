question_templates = {
    'ga1-q1': '''Install and run Visual Studio Code. In your Terminal (or Command Prompt), type code -s and press Enter. Copy and paste the entire output below. What is the output of {command}?''',
    'ga1-q2': '''
Running uv run --with httpie -- https [URL] installs the Python package httpie and sends a HTTPS request to the URL.
Send a HTTPS request to {url} with the URL encoded parameter {param} set to {email}
What is the JSON output of the command? (Paste only the JSON body, not the headers)''',
    'ga1-q3': '''Let's make sure you know how to use npx and prettier.
Download the attached file . In the directory where you downloaded it, make sure it is called {req_filename}, and run {command}
What is the output of the command?''',
    
    'ga1-q4': '''
Let's make sure you can write formulas in Google Sheets. Type this formula into Google Sheets.
{formula}
What is the result?''',

    'ga1-q5': '''
    Let's make sure you can write formulas in Microsoft Excel. Type this formula into Microsoft Excel.
Note: This will ONLY work in Office 365.
{excel_formula}
What is the result?''',

    'ga1-q6': '''{html_element}
Just above this paragraph, there's a hidden input with a secret value.
What is the value in the hidden input?''',

    'ga1-q7': '''How many {day_name} are there in the date range {start_date} to {end_date}?
The dates are in the year-month-day format. Include both the start and end date in your count. You can do this using any tool (e.g. Excel, Python, JavaScript, manually).''',

    'ga1-q8': '''Download and unzip file  which has a single {csv_file} file inside.
What is the value in the {column_name} column of the CSV file?''',

    'ga1-q9': '''Let's make sure you know how to use JSON. Sort this JSON array of objects by the value of the {first_field} field. In case of a tie, sort by the {second_field} field. Paste the resulting JSON below without any spaces or newlines.
    {json_array}''',

    'ga1-q10': '''Download and use multi-cursors and convert it into a single JSON object, where key=value pairs are converted into {key: value, key: value, ...}.
What's the result when you paste the JSON at tools-in-data-science.pages.dev/jsonhash and click the Hash button?''',

    'ga1-q11': '''Let's make sure you know how to select elements using CSS selectors. Find all {html_element}'s having a {given_class} class in the hidden element below. What's the sum of their {given_attribute} attributes?
{hidden_html}
Sum of data-value attributes:''',

    'ga1-q12': '''Download and process the files in  which contains three files with different encodings:
{file_1}: CSV file encoded in {encoding_1}
{file_2}: CSV file encoded in {encoding_2}
{file_3}: Tab-separated file encoded in {encoding_3}
Each file has 2 columns: symbol and value. Sum up all the values where the symbol matches {symbol_1} OR {symbol_2} OR {symbol_3} across all three files.
What is the sum of all values associated with these symbols?''',

    'ga1-q13': '''Let's make sure you know how to use GitHub. Create a GitHub account if you don't have one. Create a new public repository. Commit a single JSON file called {file_name} with the value {value} and push it.
Enter the raw Github URL of email.json so we can verify it. (It might look like https://raw.githubusercontent.com/[GITHUB ID]/[REPO NAME]/main/email.json.)''',

    'ga1-q14': '''Download  and unzip it into a new folder, then replace all {existing_word} (in upper, lower, or mixed case) with {new_word} in all files. Leave everything as-is - don't change the line endings.
What does running {command} in that folder show in bash?''',

    'ga1-q15': '''Download  and extract it. Use ls with options to list all files in the folder along with their date and file size.
What's the total size of all files at least {file_size_number} bytes large and modified on or after {date_string}?''',

    'qa1-q16': '''Download  and extract it. Use mv to move all files under folders into an empty folder. Then rename all files replacing each digit with the next. 1 becomes 2, 9 becomes 0, a1b9c.txt becomes a2b0c.txt.
What does running {command} in bash on that folder show?''',

    'ga1-q17': '''Download  and extract it. It has 2 nearly identical files, {file_1} and {file_2}, with the same number of lines.
How many lines are different between {file_1} and {file_2}?''',

    'ga1-q18': '''There is a tickets table in a SQLite database that has columns type, units, and price. Each row is a customer bid for a concert ticket.
{ticket_table}
What is the total sales of all the items in the {ticket_type} ticket type? Write SQL to calculate it.''',

    'ga2-q1': '''Write documentation in Markdown for an **imaginary** analysis of the number of steps you walked each day for a week, comparing over time and with friends. The Markdown must include:
{markdown_requirements}
''',

    'ga2-q2': '''Download the image below and compress it losslessly to an image that is less than 1,500 bytes. By losslessly, we mean that every pixel in the new image should be identical to the original image.
Upload your losslessly compressed image (less than 1,500 bytes)''',

    'ga2-q3': '''Publish a page using GitHub Pages that showcases your work. Ensure that your email address {email_id} is in the page's HTML.
GitHub pages are served via CloudFlare which obfuscates emails. So, wrap your email address inside a:
<!--email_off-->{email_id}<!--/email_off-->
What is the GitHub Pages URL? It might look like: https://[USER].github.io/[REPO]/''',

    'ga2-q4': '''Let's make sure you can access Google Colab. Run this program on Google Colab, allowing all required access to your email ID: {email_id}.
{python_code}
What is the result? (It should be a 5-character string)''',

    'ga2-q5': '''Download this image. Create a new Google Colab notebook and run this code (after fixing a mistake in it) to calculate the number of pixels with a certain minimum brightness:
    {python_code}
    What is the result? (It should be a number)''',

    'ga2-q6': '''Download this  which has the marks of 100 imaginary students.
Create and deploy a Python app to Vercel. Expose an API so that when a request like https://your-app.vercel.app/api?name=X&name=Y is made, it returns a JSON response with the marks of the names X and Y in the same order, like this:
{ "marks": [10, 20] }
Make sure you enable CORS to allow GET requests from any origin.
What is the Vercel URL? It should look like: https://your-app.vercel.app/api''',

    'ga2-q7': '''Create a GitHub action on one of your GitHub repositories. Make sure one of the steps in the action has a name that contains your email address {email}. For example:
jobs:
  test:
    steps:
      - name: {email}
        run: echo "Hello, world!"
Trigger the action and make sure it is the most recent action.
What is your repository URL? It will look like: https://github.com/USER/REPO''',

    'ga2-q8': '''Create and push an image to Docker Hub. Add a tag named {tag} to the image.
What is the Docker image URL? It should look like: https://hub.docker.com/repository/docker/$USER/$REPO/general''',

    'ga2-q9': '''Download . This file has 2-columns:

studentId: A unique identifier for each student, e.g. 1, 2, 3, ...
class: The class (including section) of the student, e.g. 1A, 1B, ... 12A, 12B, ... 12Z
Write a FastAPI server that serves this data. For example, /api should return all students data (in the same row and column order as the CSV file) as a JSON like this:
{instructions}
What is the API URL endpoint for FastAPI? It might look like: http://127.0.0.1:8000/api
''', 

    'ga2-q10': '''Download Llamafile. Run the Llama-3.2-1B-Instruct.Q6_K.llamafile model with it.

Create a tunnel to the Llamafile server using ngrok.

What is the ngrok URL? It might look like: https://[random].ngrok-free.app/''', #Do later

    'ga3-q1': '''One of the test cases involves sending a sample piece of meaningless text:
{meaningless_text}
Write a Python program that uses httpx to send a POST request to OpenAI's API to analyze the sentiment of this (meaningless) text into GOOD, BAD or NEUTRAL. Specifically:

Make sure you pass an Authorization header with dummy API key.
Use {model_name} as the model.
The first message must be a system message asking the LLM to analyze the sentiment of the text. Make sure you mention GOOD, BAD, or NEUTRAL as the categories.
The second message must be exactly the text contained above.
This test is crucial for DataSentinel Inc. as it validates both the API integration and the correctness of message formatting in a controlled environment. Once verified, the same mechanism will be used to process genuine customer feedback, ensuring that the sentiment analysis module reliably categorizes data as GOOD, BAD, or NEUTRAL. This reliability is essential for maintaining high operational standards and swift response times in real-world applications.

Note: This uses a dummy httpx library, not the real one. You can only use:

response = httpx.get(url, **kwargs)
response = httpx.post(url, json=None, **kwargs)
response.raise_for_status()
response.json()''',

    'ga3-q2': '''To optimize operational costs and prevent unexpected API overages, the engineering team at LexiSolve has developed an internal diagnostic tool that simulates and measures token usage for typical prompts sent to the language model.
One specific test case an understanding of text tokenization. Your task is to generate data for that test case.
Specifically, when you make a request to OpenAI's GPT-4o-Mini with just this user message:
{user_message}
... how many input tokens does it use up?''',

    'ga3-q3': '''As part of the integration process, you need to write the body of the request to an OpenAI chat completion call that:
Uses model gpt-4o-mini
Has a system message: Respond in JSON
Has a user message: Generate 10 random addresses in the US
Uses structured outputs to respond with an object addresses which is an array of objects with required fields: {required_fields} .
Sets additionalProperties to {additionalPropertiesBoolean} to prevent additional properties.
Note that you don't need to run the request or use an API key; your task is simply to write the correct JSON body.
What is the JSON body we should send to https://api.openai.com/v1/chat/completions for this? (No need to run it or to use an API key. Just write the body of the request below.)''',

    'ga3-q4': '''Your team is tasked with integrating OpenAI's vision model into the invoice processing workflow. The chosen model, gpt-4o-mini, is capable of analyzing both text and image inputs simultaneously. When an invoice is received—for example, an invoice image may contain a vendor email like alice.brown@acmeglobal.com and a transaction number such as 34921. The system needs to extract all embedded text to automatically populate the vendor management system.
The automated process will send a POST request to OpenAI's API with two inputs in a single user message:
Text: A simple instruction {text_instruction}
Image URL: A base64 URL representing the invoice image that might include the email and the transaction number among other details.
Here is an example invoice image:
Write just the JSON body (not the URL, nor headers) for the POST request that sends these two pieces of content (text and image URL) to the OpenAI API endpoint.
Use gpt-4o-mini as the model.
Send a single user message to the model that has a text and an image_url content (in that order).
The text content should be {text_instruction}
Send the image_url as a base64 URL of the image above. CAREFUL: Do not modify the image.
Write your JSON body here:''',

    'ga3-q5': '''Imagine you are working on the SecurePay team as a junior developer tasked with integrating the text embeddings feature into the fraud detection module. When a user initiates a transaction, the system sends a personalized verification message to the user's registered email address. This message includes the user's email address and a unique transaction code (a randomly generated number). Here are 2 verification messages:
{verification_message_1}
{verification_message_2}
The goal is to capture this message, convert it into a meaningful embedding using OpenAI's text-embedding-3-small model, and subsequently use the embedding in a machine learning model to detect anomalies.
Your task is to write the JSON body for a POST request that will be sent to the OpenAI API endpoint to obtain the text embedding for the 2 given personalized transaction verification messages above. This will be sent to the endpoint https://api.openai.com/v1/embeddings.
Write your JSON body here:''',

    'ga3-q6': '''As part of a pilot project, ShopSmart has curated a collection of 25 feedback phrases that represent a variety of customer sentiments. Examples of these phrases include comments like “Fast shipping and great service,” “Product quality could be improved,” “Excellent packaging,” and so on. Due to limited processing capacity during initial testing, you have been tasked with determine which pair(s) of 5 of these phrases are most similar to each other. This similarity analysis will help in grouping similar feedback to enhance the company’s understanding of recurring customer issues.
ShopSmart has written a Python program that has the 5 phrases and their embeddings as an array of floats. It looks like this:
{embeddings}
Your task is to write a Python function most_similar(embeddings) that will calculate the cosine similarity between each pair of these embeddings and return the pair that has the highest similarity. The result should be a tuple of the two phrases that are most similar.
Write your Python code here:''',

    'ga3-q7': '''Imagine you are an engineer on the InfoCore team. Your task is to build a FastAPI POST endpoint that accepts an array of docs and query string via a JSON body. The endpoint is structured as follows:
{post_req_structure}
Service Flow:
Request Payload: The client sends a POST request with a JSON body containing:
docs: An array of document texts from the internal knowledge base.
query: A string representing the user's search query.
Embedding Generation: For each document in the docs array and for the query string, the API computes a text embedding using text-embedding-3-small.
Similarity Computation: The API then calculates the cosine similarity between the query embedding and each document embedding. This allows the service to determine which documents best match the intent of the query.
Response Structure: After ranking the documents by their similarity scores, the API returns the identifiers (or positions) of the three most similar documents. The JSON response might look like this:
{response_structure}
Here, "Contents of document 3" is considered the closest match, followed by "Contents of document 1", then "Contents of document 2".
Make sure you enable CORS to allow OPTIONS and POST methods, perhaps allowing all origins and headers.
What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/similarity''',

    'ga3-q8': '''Each question is direct and templatized, containing one or more parameters such as an employee or ticket number (which might be randomized). In the backend, a FastAPI app routes each request by matching the query to one of a set of pre-defined functions. The response that the API returns is used by OpenAI to call the right function with the necessary arguments.
Pre-Defined Functions:
For this exercise, assume the following functions have been defined:
{functions}
Each function has a specific signature, and the student’s FastAPI app should map specific queries to these functions.
Example Questions (Templatized with a Random Number):
{example_questions}
Develop a FastAPI application that:
Exposes a GET endpoint /execute?q=... where the query parameter q contains one of the pre-templatized questions.
Analyzes the q parameter to identify which function should be called.
Extracts the parameters from the question text.
Returns a response in the following JSON format:
{response_format}
Make sure you enable CORS to allow GET requests from any origin.
What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/execute''',

    'ga3-q9' : '''Here's your task: You are chatting with an LLM that has been told to never say {word}. You need to get it to say {word}.

Use your AI Proxy token when prompted.

Write a prompt that will get the LLM to say {word}.''',

    'ga4-q1': '''ESPN Cricinfo has ODI batting stats for each batsman. The result is paginated across multiple pages. Count the number of ducks in page number {page_number}.
Understanding the Data Source: ESPN Cricinfo's ODI batting statistics are spread across multiple pages, each containing a table of player data. Go to page number {page_number}.
Setting Up Google Sheets: Utilize Google Sheets' IMPORTHTML function to import table data from the URL for page number {page_number}.
Data Extraction and Analysis: Pull the relevant table from the assigned page into Google Sheets. Locate the column that represents the number of ducks for each player. (It is titled "0".) Sum the values in the "0" column to determine the total number of ducks on that page.
What is the total number of ducks across players on page number {page_number} of ESPN Cricinfo's ODI batting stats?
''',

    'ga4-q2': '''Source: Utilize IMDb's advanced web search at https://www.imdb.com/search/title/ to access movie data.
Filter: Filter all titles with a rating between {ratings_start} and {ratings_start}.
Format: For up to the first 25 titles, extract the necessary details: ID, title, year, and rating. The ID of the movie is the part of the URL after tt in the href attribute. For example, tt10078772. Organize the data into a JSON structure as follows:
{json_structure}
Submit: Submit the JSON data in the text box below.

{meaningless_text}

What is the JSON data?
''',

    'ga4-q3': '''Write a web application that exposes an API with a single query parameter: ?country=. It should fetch the Wikipedia page of the country, extracts all headings (H1 to H6), and create a Markdown outline for the country. The outline should look like this:
{markdown_outline}
API Development: Choose any web framework (e.g., FastAPI) to develop the web application. Create an API endpoint (e.g., /api/outline) that accepts a country query parameter.
Fetching Wikipedia Content: Find out the Wikipedia URL of the country and fetch the page's HTML.
Extracting Headings: Use an HTML parsing library (e.g., BeautifulSoup, lxml) to parse the fetched Wikipedia page. Extract all headings (H1 to H6) from the page, maintaining order.
Generating Markdown Outline: Convert the extracted headings into a Markdown-formatted outline. Headings should begin with #.
Enabling CORS: Configure the web application to include appropriate CORS headers, allowing GET requests from any origin.
What is the URL of your API endpoint?''',

'ga4-q4': '''As part of this initiative, you are tasked with developing a system that automates the following:
API Integration and Data Retrieval: Use the BBC Weather API to fetch the weather forecast for Mumbai. Send a GET request to the locator service to obtain the city's locationId. Include necessary query parameters such as API key, locale, filters, and search term (city).
Weather Data Extraction: Retrieve the weather forecast data using the obtained locationId. Send a GET request to the weather broker API endpoint with the locationId.
Data Transformation: Extract the localDate and enhancedWeatherDescription from each day's forecast. Iterate through the forecasts array in the API response and map each localDate to its corresponding enhancedWeatherDescription. Create a JSON object where each key is the localDate and the value is the enhancedWeatherDescription.
The output would look like this:
{json_format}
What is the JSON weather forecast description for {required_city}?''',

    'ga4-q5': '''What is the maximum latitude of the bounding box of the city Tehran in the country Iran on the Nominatim API?
API Integration: Use the Nominatim API to fetch geospatial data for a specified city within a country via a GET request to the Nominatim API with parameters for the city and country. Ensure adherence to Nominatim’s usage policies, including rate limiting and proper attribution.
Data Retrieval and Filtering: Parse the JSON response from the API. If multiple results are returned (e.g., multiple cities named “Springfield” in different states), filter the results based on the provided osm_id ending to select the correct city instance.
Parameter Extraction: Access the boundingbox attribute. Depending on whether you're looking for the minimum or maximum latitude, extract the corresponding latitude value.
Impact
By automating the extraction and processing of bounding box data, UrbanRide can:
Optimize Routing: Enhance route planning algorithms with precise geographical boundaries, reducing delivery times and operational costs.
Improve Fleet Allocation: Allocate vehicles more effectively across defined service zones based on accurate city extents.
Enhance Market Analysis: Gain deeper insights into regional performance, enabling targeted marketing and service improvements.
Scale Operations: Seamlessly integrate new cities into their service network with minimal manual intervention, ensuring consistent data quality.
What is the {maximum_or_minimum} latitude of the bounding box of the city {city_name} in the country {country_name} on the Nominatim API? Value of the {maximum_or_minimum} latitude''',

    'ga4-q6': '''Search using the Hacker News RSS API for the latest Hacker News post mentioning {mentioning_word} and having a minimum of {minimum_points} points. What is the link that it points to?
Automate Data Retrieval: Utilize the HNRSS API to fetch the latest Hacker News posts. Use the URL relevant to fetching the latest posts, searching for topics and filtering by a minimum number of points.
Extract and Present Data: Extract the most recent <item> from this result. Get the <link> tag inside it.
Share the result: Type in just the URL in the answer.
What is the link to the latest Hacker News post mentioning {mentioning_word} having at least {minimum_points} points?''',

    'ga4-q7': '''Using the GitHub API, find all users located in the city {city_name} with over {followers_count} followers.
When was the newest user's GitHub profile created?
API Integration and Data Retrieval: Leverage GitHub’s search endpoints to query users by location and filter them by follower count.
Data Processing: From the returned list of GitHub users, isolate those profiles that meet the specified criteria.
Sort and Format: Identify the "newest" user by comparing the created_at dates provided in the user profile data. Format the account creation date in the ISO 8601 standard (e.g., "2024-01-01T00:00:00Z").
Enter the date (ISO 8601, e.g. "2024-01-01T00:00:00Z") when the newest user joined GitHub.
''', 

    'ga4-q8': '''Create a scheduled GitHub action that runs daily and adds a commit to your repository. The workflow should:
Use schedule with cron syntax to run once per day (must use specific hours/minutes, not wildcards)
Include a step with your email {email} in its name
Create a commit in each run
Be located in .github/workflows/ directory
After creating the workflow:
Trigger the workflow and wait for it to complete
Ensure it appears as the most recent action in your repository
Verify that it creates a commit during or within 5 minutes of the workflow run
Enter your repository URL (format: https://github.com/USER/REPO):''',

'ga4-q9': '''
This file,  contains a table of student marks in Maths, Physics, English, Economics, and Biology.

Calculate the total Maths marks of students who scored {min_marks} or more marks in {subject} in groups {groupa}-{groupb} (including both groups).
{instruction}

What is the total Maths marks of students who scored {min_marks} or more marks in {subject} in groups {groupa}-{groupb} (including both groups)?
''',

'ga4-q10': '''
As part of the Documentation Transformation Project, you are a junior developer at EduDocs tasked with developing a streamlined workflow for converting PDF files to Markdown and ensuring their consistent formatting. This project is critical for supporting EduDocs' commitment to delivering high-quality, accessible educational resources to its clients.
{meainingless_text}

What is the markdown content of the PDF, formatted with prettier@3.4.2?
''',

'ga5-q1': '''
{instructions}
What is the total margin for transactions before {date} for {product} sold in {country} (which may be spelt in different ways)?
''',

'ga5-q2': '''
As a data analyst at EduTrack Systems, your task is to process this text file and determine the number of unique students based on their student IDs. This deduplication is essential to:

instructions
Download the text file with student marks 
{file}
How many unique students are there in the file?
''',

'ga5-q3': '''
s-anand.net is a personal website that had region-specific music content. One of the site's key sections is {language}, which hosts music files and is especially popular among the local audience. The website is powered by robust Apache web servers that record detailed access logs. These logs are essential for understanding user behavior, server load, and content engagement.
{meaningless_text}

What is the number of successful GET requests for pages under {language} from {start} until before {end} on {day}?
''',

'ga5-q4': '''
s-anand.net is a personal website that had region-specific music content. One of the site's key sections is malayalam, which hosts music files and is especially popular among the local audience. The website is powered by robust Apache web servers that record detailed access logs. These logs are essential for understanding user behavior, server load, and content engagement.

{meaningless_text}

Across all requests under {language} on {date}, how many bytes did the top IP address (by volume of downloads) download?
''',

'ga5-q5' : '''
GlobalRetail Insights is a market research and analytics firm specializing in providing data-driven insights for multinational retail companies. Their clients rely on accurate, detailed sales reports to make strategic decisions regarding product placement, inventory management, and marketing campaigns. However, the quality of these insights depends on the reliability of the underlying sales data.
{meaningless_text}

How many units of {product} were sold in {city} on transactions with at least {min_units} units?
''',

'ga5-q6': '''
ReceiptRevive Analytics is a data recovery and business intelligence firm specializing in processing legacy sales data from paper receipts. Many of the client companies have archives of receipts from past years, which have been digitized using OCR (Optical Character Recognition) techniques. However, due to the condition of some receipts (e.g., torn, faded, or partially damaged), the OCR process sometimes produces incomplete JSON data. These imperfections can lead to truncated fields or missing values, which complicates the process of data aggregation and analysis.

{meaningless_text}
As a data recovery analyst at ReceiptRevive Analytics, your task is to develop a program that will:

{instructions}

What is the total sales value?
''',

'ga5-q7': '''
DataSure Technologies is a leading provider of IT infrastructure and software solutions, known for its robust systems and proactive maintenance practices. As part of their service offerings, DataSure collects extensive logs from thousands of servers and applications worldwide. These logs, stored in JSON format, are rich with information about system performance, error events, and user interactions. However, the logs are complex and deeply nested, which can make it challenging to quickly identify recurring issues or anomalous behavior.

{meaningless_text}

As a data analyst at DataSure Technologies, you have been tasked with developing a script that processes a large JSON log file and counts the number of times a specific key, represented by the placeholder {command}, appears in the JSON structure. Your solution must

{instructions}

How many times does {command} appear as a key?
''',

'ga5-q8': '''
EngageMetrics is a digital marketing analytics firm that specializes in tracking and analyzing social media engagement. Their clients, ranging from major brands to local businesses, rely on data-driven insights to optimize content strategy, measure campaign performance, and identify posts that drive significant user interaction.

{meaningless_text}

Write a DuckDB SQL query to find all posts IDs after {date_time} with at least {x} comment with {y} useful stars, sorted. The result should be a table with a single column called post_id, and the relevant post IDs should be sorted in ascending order.
''',

'ga5-q9': '''
Mystery Tales Publishing is an independent publisher specializing in mystery and suspense audiobooks. To broaden their audience and improve accessibility, they have been uploading narrated versions of their stories to YouTube. In addition to reaching visually impaired users, they want to leverage transcripts for content summarization, search indexing, and social media promotion.

{meaningless_text}

What is the text of the transcript of this Mystery Story Audiobook between {x} and {y} seconds?
''',

'ga5-q10': '''
 As a digital forensics analyst at PixelGuard Solutions, your task is to reconstruct the original image from its scrambled pieces. You are provided with:
 
The 25 individual image pieces (put together as a single image).
A mapping file detailing the original (row, col) position for each piece and its current (row, col) location.

{meaningless_text}

Upload the reconstructed image by moving the pieces from the scrambled position to the original position:
'''
}