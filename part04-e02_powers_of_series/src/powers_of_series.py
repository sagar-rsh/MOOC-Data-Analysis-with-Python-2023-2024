#!/usr/bin/env python3

import pandas as pd

def powers_of_series(s, k):
    # c=[ s**i for i in range(1,k+1) ]
    # df = pd.DataFrame(dict(zip(range(1,k+1), c)))

    df = pd.DataFrame([s]*k).T
    df.columns = pd.RangeIndex(1, k+1)
    pwr_df = df**df.columns

    return pwr_df
    
def main():
    s = pd.Series([1,2,3,4], index=list("abcd"))

    print(powers_of_series(s, 4))
    
if __name__ == "__main__":
    main()
