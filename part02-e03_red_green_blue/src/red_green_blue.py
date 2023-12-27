#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    with open(filename, "r") as f:
        lines = f.readlines()

    result = []
    pattern = r"(\d{1,3})\s*(\d{1,3})\s*(\d{1,3})\s*([a-zA-Z0-9]+\s?[a-zA-Z0-9]+)"
    for line in lines[1:]:
        match = re.search(pattern, line)
        if match:
            g = match.groups()
            result.append(f"{g[0]}\t{g[1]}\t{g[2]}\t{g[3]}")
        else:
            print(match, line)

    return result

def main():
    print(red_green_blue())

if __name__ == "__main__":
    main()
