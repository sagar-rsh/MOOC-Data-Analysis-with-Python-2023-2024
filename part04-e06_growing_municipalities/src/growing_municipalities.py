#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    # c="Population change from the previous year, %"
    # n = len(df)
    # k = sum(df[c] > 0.0)
    # return k / n
    mask = df["Population change from the previous year, %"] >0.0
    incr_population = df[mask].shape[0]

    return incr_population/df.shape[0]

def main():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    municipalty_df = df["Akaa": "Äänekoski"]

    proportion = growing_municipalities(municipalty_df)
    # print(f"Proportion of growing municipalities: {proportion:.1%}")
    print(f"Proportion of growing municipalities: {proportion*100:.1f}%")
if __name__ == "__main__":
    main()
