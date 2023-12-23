#!/usr/bin/env python3

def reverse_dictionary(d):
    rev_d = {}
    for key, val in d.items():
        rev_pair = dict.fromkeys(val, [key])
        for k, v in rev_pair.items():
            rev_d.setdefault(k, []).extend(v)

    return rev_d

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
