#!/usr/bin/env python3

def extract_numbers(s):
    l = s.split()
    result = []
    
    for val in l:
        try:
            val = int(val)
            result.append(val)
        except ValueError:
            try:
                val = float(val)
                result.append(val)
            except ValueError:
                print("Not a number")


    return result

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
