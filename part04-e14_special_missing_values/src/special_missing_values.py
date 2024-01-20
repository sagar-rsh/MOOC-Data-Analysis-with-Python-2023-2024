#!/usr/bin/env python3

import pandas as pd
import numpy as np

def special_missing_values():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    # df["LW"].replace(["New", "Re"], np.nan, inplace=True)
    # df["LW"] = df["LW"].astype("float")

    df["LW"] = pd.to_numeric(df["LW"], errors ='coerce') 
    mask = df["Pos"] > df["LW"]

    return df[mask]

def main():
    print(special_missing_values())

if __name__ == "__main__":
    main()
