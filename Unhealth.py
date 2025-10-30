import sys
for line in sys.stdin:
    if "Unhealthy" in line:
        print(line.strip())
