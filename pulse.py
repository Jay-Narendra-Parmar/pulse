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
latency = ((ending_time-starting_time)*1000)

print(response.status_code)
print(response.reason_phrase)

print(f"Status: {response.status_code} {response.reason_phrase}")
print(f"Latency: {latency:.1f} ms")

print("\nResponse Headers:")

# Tells the client how the response can be cached.
print("Cache-Control:", response.headers.get("cache-control", "not present"))

# Tells the browser to use HTTPS for future requests.
print("Strict-Transport-Security:", response.headers.get("strict-transport-security", "not present"))

# Tells the client the media type of the response body.
print("Content-Type:", response.headers.get("content-type", "not present"))