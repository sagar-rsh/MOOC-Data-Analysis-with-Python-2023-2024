#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    result = []

    pattern = r"(\d+)\s*(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s*(\d{1,2})\s*(\d{2}):(\d{2})\s*(.*)"
    with open(filename, "r") as f:
        for line in f:
            match = re.search(pattern, line)
            if match:
                result.append((int(match.group(1)), match.group(2), int(match.group(3)), int(match.group(4)), int(match.group(5)), match.group(6)))

    
    return result

def main():
    print(file_listing())

if __name__ == "__main__":
    main()
