#!/usr/bin/env python3

import sys

def file_count(filename):
    with open(filename, "r") as f:
        data = f.read()
        linecount = len(data.strip().split('\n'))
        wordcount = len(data.split())
        # print(data.split())
        charactercount = len(data)

    return linecount, wordcount, charactercount


def main():
    for filename in sys.argv[1:]:
        counts = file_count("src/test.txt")
        print(f"{counts[0]}\t{counts[1]}\t{counts[2]}\t{filename}")

if __name__ == "__main__":
    main()
