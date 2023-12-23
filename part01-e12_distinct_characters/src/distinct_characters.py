#!/usr/bin/env python3

def distinct_characters(L):
    d = {}
    for val in L:
        d[val] = len(set(val))
        
    return d

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
