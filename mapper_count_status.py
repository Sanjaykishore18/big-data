import sys

for line in sys.stdin:
    fields = line.strip().split(",")
    # Adjust the index if needed; assuming TargetHealthStatus is at -2 (second last column)
    status = fields[-2].strip()
    print(f"{status}\t1")
