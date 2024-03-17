#!/usr/bin/python3
import sys

# Initialize variables
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    # Read stdin line by line
    for line in sys.stdin:
        # Split line into its components
        parts = line.split()
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        # Update total file size
        total_size += file_size

        # Update status code counts
        if status_code in status_counts:
            status_counts[status_code] += 1

        # Increment line count
        line_count += 1

        # Check if 10 lines have been processed
        if line_count % 10 == 0:
            # Print statistics
            print(f"File size: {total_size}")
            for code, count in sorted(status_counts.items()):
                if count > 0:
                    print(f"{code}: {count}")
            print()

except KeyboardInterrupt:
    # Handle keyboard interruption
    print(f"File size: {total_size}")
    for code, count in sorted(status_counts.items()):
        if count > 0:
            print(f"{code}: {count}")
    sys.exit(0)

