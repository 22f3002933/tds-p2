import json
import re

# Path to the JSONL file
file_path = "q-parse-partial-json.jsonl"
total_sales = 0


# Regex pattern to capture 'sales' values
sales_pattern = re.compile(r'"sales"\s*:\s*(\d+)')

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        try:
            # Extract 'sales' value using regex
            match = sales_pattern.search(line)
            if match:
                sales_value = int(match.group(1))  # Convert to integer
                total_sales += sales_value  # Add to total
        except Exception as e:
            # Log or print error if needed
            continue

print("Total Sales Value:", total_sales)