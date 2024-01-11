#!/usr/bin/env python3
import pandas as pd

def read_series():
    indexes = []
    values = []
    
    while True:
        line = input()
        if not line.strip():
            break
        try:
            idx, val = line.split()
            indexes.append(idx)
            values.append(val)
        except ValueError as e:
            print(e)

    return pd.Series(values, index= indexes, dtype=object)

def main():
    print(read_series())
        

if __name__ == "__main__":
    main()
