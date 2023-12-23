#!/usr/bin/env python3

def triple(val):
    return val *3

def square(val):
    return val**2

def main():
    for val in range(1, 11):
        triple_val = triple(val)
        square_val = square(val)
        if square_val > triple_val:
            break

        print(f"triple({val})=={triple_val} square({val})=={square_val}")

if __name__ == "__main__":
    main()
