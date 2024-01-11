#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    values = s.values
    indices = s.index

    return pd.Series(indices, index=values)

def main():
    s = pd.Series([1,2,3,2], index=list("abca"))

    inv_s = inverse_series(s)
    print(inv_s[2])

if __name__ == "__main__":
    main()
