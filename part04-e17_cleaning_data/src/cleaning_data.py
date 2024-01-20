#!/usr/bin/env python3

import pandas as pd
import numpy as np


# def fix_name_field(s):
#     s = s.str.replace(r"(\w+), *(\w+)", r"\2 \1")
#     return s

# def cleaning_data():
#     df = pd.read_csv("src/presidents.tsv", sep="\t")
#     df = df.where(df != "two", 2)
#     df['Start'] = df['Start'].str.extract(r'^(\d{4})', expand=False)
#     df = df.where(df != "-", np.nan)
#     df["President"] = fix_name_field(df["President"])
#     df["Vice-president"] = fix_name_field(df["Vice-president"]).str.title()
#     return df.astype({"President":object, "Start":int,  "Last":float,
#                       "Seasons":int, "Vice-president": object})

def cleaning_data():
    df = pd.read_csv("src/presidents.tsv", sep="\t")

    df["President"] = df["President"].str.replace(",", "").str.title()
    df.loc[2:, "President"] = df.loc[2:, "President"].str.split().apply(lambda x: ' '.join(x[::-1]))
    df["Vice-president"] = df["Vice-president"].str.replace(",", "").str.title()
    df.loc[2:, "Vice-president"] = df.loc[2:, "Vice-president"].str.split().apply(lambda x: ' '.join(x[::-1]))

    df["Start"] = df["Start"].str.split().str.get(0)
    df["Last"] = pd.to_numeric(df["Last"], errors="coerce")

    df["Seasons"] = df["Seasons"].str.replace("two", "2", regex=False)

    df = df.astype({"President": object, "Start": "int", "Last": "float", "Seasons": int, "Vice-president": object})

    return df

def main():
    df = cleaning_data()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)

if __name__ == "__main__":
    main()
