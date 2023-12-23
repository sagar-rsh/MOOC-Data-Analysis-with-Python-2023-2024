#!/usr/bin/env python3


def main():
    for row in range(1, 11):
        for col in range(1, 11):
            print(f"{row * col}", end="\t")
        print()

if __name__ == "__main__":
    main()
