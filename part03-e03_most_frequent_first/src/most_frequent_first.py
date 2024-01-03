#!/usr/bin/env python3

import numpy as np

def most_frequent_first(a, c):
    # b = a[:,c]   # get column c
    # _,s,t = np.unique(b, return_inverse=True, return_counts=True)
    # idx = np.argsort(t[s])
    # return a[idx][::-1]
    
    selected_col = a[:, c]
    unique_elements, frequency = np.unique(selected_col, return_counts=True)
    sorted_indexes = np.argsort(frequency)[::-1]
    sorted_by_freq = unique_elements[sorted_indexes]

    d = {k: v for v, k in enumerate(sorted_by_freq)}
    order = np.argsort([d[key] for key in selected_col])

    return a[order]

def main():
    np.random.seed(2)
    a = np.random.randint(0, 10, (6,6))
    print(f"a: {a}")
    print(most_frequent_first(a, -1))

if __name__ == "__main__":
    main()
