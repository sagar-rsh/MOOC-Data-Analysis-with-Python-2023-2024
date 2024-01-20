#!/usr/bin/env python3

import pandas as pd
import numpy as np

def last_week():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    df["LW"] = pd.to_numeric(df["LW"], errors="coerce")
    df["New Pos"] = df["Pos"].copy()

    res_df = pd.merge(df.iloc[:, 0], df.iloc[:, 1:], left_on="Pos", right_on="LW", how="left")
    res_df["LW"] = np.nan

    mask = (res_df["New Pos"] == res_df["Peak Pos"]) & (res_df["New Pos"] != res_df["Pos"])
    res_df.loc[mask, "Peak Pos"] = np.nan

    res_df["WoC"] = res_df["WoC"] - 1

    return res_df.iloc[:, :-1]

def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
