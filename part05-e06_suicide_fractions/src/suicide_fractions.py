#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    df = pd.read_csv("src/who_suicide_statistics.csv")

    # df["Suicide fraction"] = df["suicides_no"] / df["population"]
    # result = df.groupby("country").mean()
    # return result["Suicide fraction"]
    
    suicide_fractions = pd.concat([df["country"], df["suicides_no"]/df["population"]], axis=1)

    return suicide_fractions.groupby("country")[0].mean()


def main():
    df = suicide_fractions()
    print("Shape:", df.shape)
    print(df.head())
    

if __name__ == "__main__":
    main()
