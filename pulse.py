import sys
import httpx 
import time

if len(sys.argv) < 2:
    print("Usage: python pulse.py <url>")
    sys.exit(1)

url = sys.argv[1]

if url.strip() == "":
    print("String is empty")
    sys.exit(1)

print(url)

starting_time = time.perf_counter()
response = httpx.get(url, timeout = 10)
ending_time = time.perf_counter()
print((ending_time-starting_time)*1000)

print(response.status_code)
print(response.reason_phrase)
print(response.elapsed)