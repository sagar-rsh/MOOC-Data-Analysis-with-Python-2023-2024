#!/usr/bin/env python3

def word_frequencies(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    d = {}
    for line in lines:
        words_list = list(map(lambda x: x.strip("""!"#$%&'()*,-./:;?@[]_""") , line.split()))

        for key in words_list:
            d[key] = d.setdefault(key, 0) + 1
        

    return d

def main():
    d = word_frequencies("src/alice.txt")
    for key, val in d.items():
        print(key, val, sep="\t")

if __name__ == "__main__":
    main()
