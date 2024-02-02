#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    groups = df.groupby("Publisher")
    top_publisher = groups["WoC"].sum().idxmax()

    return groups.get_group(top_publisher)

def main():
    df = best_record_company()
    print("Shape:", df.shape)
    print("Column names:\n", df.columns)
    print(df.head())
    

if __name__ == "__main__":
    main()
