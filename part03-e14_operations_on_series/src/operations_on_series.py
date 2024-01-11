#!/usr/bin/env python3
import pandas as pd
import numpy as np

def create_series(L1, L2):
    s1 = pd.Series(L1, index=list("abc"))
    s2 = pd.Series(L2, index=list("abc"))

    return (s1, s2)
    
def modify_series(s1, s2):
    s1["d"] = s2["b"].copy()
    del s2["b"]

    return (s1, s2)
    
def main():
    s1, s2 = create_series(np.arange(0, 3), np.arange(3, 6))
    print(s1, s2, sep="\n")

    s3, s4 = modify_series(s1, s2)
    print(s3, s4, sep="\n")
    print(s3+s4)
    
if __name__ == "__main__":
    main()
