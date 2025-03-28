import json

def count_key_occurrences(data, target_key="FF"):
    count = 0
    if isinstance(data, dict):
        count += sum(1 for key in data if key == target_key)  # Count key matches
        for value in data.values():
            count += count_key_occurrences(value, target_key)
    elif isinstance(data, list):
        for item in data:
            count += count_key_occurrences(item, target_key)
    return count

# Load JSON file and process
with open("your_file.json", "r", encoding="utf-8") as file:
    data = json.load(file)

ff_count = count_key_occurrences(data)
print(f"Occurrences of 'FF' as a key: {ff_count}")
