import re

def count_unique_students(txt_file_path: str) -> int:
    """
    Count unique students from the student marks text file.
    
    Args:
        txt_file_path: Path to the text file containing student records
        
    Returns:
        int: Number of unique student IDs
    Handles formats:
        1. NAME  -  ID:Marks NUMBER
        2. NAME - IDMarks NUMBER
        3. NAME - ID:MarksNumber
    """
    unique_students = set()
    
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            match = re.search(r'([A-Z0-9]+):?Marks?', line)  # Extract student ID
            if match:
                student_id = match.group(1)  # Get the matched student ID
                unique_students.add(student_id)
    
    return len(unique_students)

# Test with sample data
if __name__ == "__main__":
    file_path = "./q-clean-up-student-marks.txt"
    unique_count = count_unique_students(file_path)
    print(f"Number of unique students: {unique_count}")
    