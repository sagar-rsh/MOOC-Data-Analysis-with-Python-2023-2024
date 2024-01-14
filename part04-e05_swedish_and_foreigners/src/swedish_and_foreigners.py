#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    municipalty_df = df["Akaa": "Äänekoski"]
    mask = ((municipalty_df["Share of Swedish-speakers of the population, %"] >5) & 
            (municipalty_df["Share of foreign citizens of the population, %"] >5))
    
    final_df = municipalty_df[mask].loc[:, ["Population", "Share of Swedish-speakers of the population, %", "Share of foreign citizens of the population, %"]]

    return final_df

def main():
    print(swedish_and_foreigners())

if __name__ == "__main__":
    main()
