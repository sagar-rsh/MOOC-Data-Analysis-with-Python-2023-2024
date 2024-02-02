#!/usr/bin/env python3

import pandas as pd

def top_bands():
    uk_top40_df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    bands_df = pd.read_csv("src/bands.tsv", sep="\t")

    uk_top40_df = uk_top40_df.dropna(axis=0, how="all").dropna(axis=1, how="all")
    bands_df = bands_df.dropna(axis=0, how="all").dropna(axis=1, how="all")

    uk_top40_df["Artist"] = uk_top40_df["Artist"].str.lower()
    bands_df["Band"] = bands_df["Band"].str.lower()

    res_df = pd.merge(uk_top40_df, bands_df, left_on="Artist", right_on="Band")

    return res_df

def main():
    df = top_bands()
    print("Shape:", df.shape)
    print("Column names:\n", df.columns)
    print(df.head())

if __name__ == "__main__":
    main()
