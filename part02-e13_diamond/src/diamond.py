#!/usr/bin/env python3

import numpy as np

def diamond(n):
    if not n:
        return np.array([])
    
    top_left = np.eye(n, dtype=int)
    top_right = np.concatenate((top_left[::-1], top_left[:,1:]), axis=1)
    result = np.concatenate((top_right, top_right[::-1][1:,:]), axis=0) #mirror

    return result

def main():
    print(diamond(3))

if __name__ == "__main__":
    main()
