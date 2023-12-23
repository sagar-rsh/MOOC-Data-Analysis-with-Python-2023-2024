#!/usr/bin/env python3

def find_matching(L, pattern):
    idx_found = []
    for idx, val in enumerate(L):
        if pattern in val:
            idx_found.append(idx)

    return idx_found

def main():
    pass

if __name__ == "__main__":
    main()
