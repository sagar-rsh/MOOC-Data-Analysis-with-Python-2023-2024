#!/usr/bin/env python3

def transform(s1, s2):
    l1 = map(int, s1.split())
    l2 = map(int, s2.split())

    return list(map(lambda x: x[0]*x[1], zip(l1, l2)))

def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()
