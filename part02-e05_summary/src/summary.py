#!/usr/bin/env python3

import sys
from math import sqrt

def summary(filename):
    with open(filename, "r") as f:
        data_list = [float(x) for x in f.read().split() if not x.isalpha()]
        # print(data_list)
        sum_list = sum(data_list)
        avg_list = sum_list/len(data_list)
        std = sqrt(sum(pow(x-avg_list,2) for x in data_list) / (len(data_list) - 1))

    return sum_list, avg_list, std

def main():
    for filename in sys.argv[1:]:
        sum_v, avg_v, std = summary(filename)
        print(f"File: {filename} Sum: {sum_v:.6f} Average: {avg_v:.6f} Stddev: {std:.6f}")

if __name__ == "__main__":
    main()
