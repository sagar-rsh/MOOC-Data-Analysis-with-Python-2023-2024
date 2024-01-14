#!/usr/bin/env python3

import pandas as pd

def main():
    df = pd.read_csv("src/municipal.tsv", sep='\t')
    cols = df.columns.tolist()
    # print("Shape: {}, {}".format(*df.shape))
    print(f"Shape: {df.shape[0]},{df.shape[1]}")
    print(f"Columns:", "\n".join(cols), sep="\n")
          


if __name__ == "__main__":
    main()  
