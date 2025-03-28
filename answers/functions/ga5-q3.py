import gzip
import re
from datetime import datetime

def count_successful_get_requests(log_file):
    successful_requests = 0
    
    with gzip.open(log_file, 'rt', encoding='utf-8') as file:
        for line in file:
            # Extract time, request method, URL, and status code
            match = re.search(r'\[(\d+/[A-Za-z]+/\d+:\d+:\d+:\d+)\s[+-]\d{4}\] "(\w+)\s(/telugu/.*?)\sHTTP/\d\.\d" (\d+)', line)
            
            if match:
                timestamp, method, url, status = match.groups()
                status = int(status)

                # Ensure it's a GET request and a successful response (200-299)
                if method == "GET" and 200 <= status < 300:
                    # Convert timestamp to a datetime object
                    log_time = datetime.strptime(timestamp, "%d/%b/%Y:%H:%M:%S")

                    # Check if it's Sunday and within time range (0:00 to before 22:00)
                    if log_time.weekday() == 6 and log_time.hour < 22:  # Sunday = 6 in Python
                        successful_requests += 1

    return successful_requests

# Example usage:
log_file_path = "apache_logs.gz"  # Replace with actual file path
result = count_successful_get_requests(log_file_path)
print(f"Number of successful GET requests for /telugu/ on Sundays (0:00 - 21:59): {result}")
