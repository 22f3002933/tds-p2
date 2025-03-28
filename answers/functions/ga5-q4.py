import gzip
import re
from collections import defaultdict

def find_top_ip(log_file):
    ip_data_usage = defaultdict(int)  # Dictionary to store total bytes per IP
    target_date = "23/May/2024"

    with gzip.open(log_file, 'rt', encoding='utf-8') as file:
        for line in file:
            # Regex to extract IP, date, request URL, and size
            match = re.search(r'^(\S+) \S+ \S+ \[(\d+/[A-Za-z]+/\d+):\d+:\d+:\d+ [+-]\d{4}\] "(\w+) (/malayalam/.*?) HTTP/\d\.\d" \d+ (\d+)', line)

            if match:
                ip, date, method, url, size = match.groups()
                size = int(size)

                # Filter only for the target date and GET requests
                if date == target_date and method == "GET":
                    ip_data_usage[ip] += size

    # Find the IP with the maximum download volume
    top_ip, max_bytes = max(ip_data_usage.items(), key=lambda x: x[1])
    
    return top_ip, max_bytes

# Example usage:
log_file_path = "apache_logs.gz"  # Replace with actual file path
top_ip, total_bytes = find_top_ip(log_file_path)
print(f"Top IP: {top_ip}, Total Bytes Downloaded: {total_bytes}")
