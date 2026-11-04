import sys

if len(sys.argv) < 2:
    print("Usage: python pulse.py <url>")
    sys.exit(1)

url = sys.argv[1]

if url.strip() == "":
    print("String is empty")
    sys.exit(1)

print(url)