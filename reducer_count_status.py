import sys

current_status = None
current_count = 0

for line in sys.stdin:
    status, count = line.strip().split("\t")
    count = int(count)
    if current_status == status:
        current_count += count
    else:
        if current_status:
            print(f"{current_status}\t{current_count}")
        current_status = status
        current_count = count

# Print last status
if current_status:
    print(f"{current_status}\t{current_count}")
