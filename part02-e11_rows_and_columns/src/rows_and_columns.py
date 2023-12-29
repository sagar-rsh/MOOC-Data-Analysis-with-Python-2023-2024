#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    list_rows = []
    for row in a:
        list_rows.append(row)
    
    return list_rows

def get_columns(a):
    return [row for row in a.T]

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()
