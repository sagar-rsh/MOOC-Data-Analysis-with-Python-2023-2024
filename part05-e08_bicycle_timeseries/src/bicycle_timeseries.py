#!/usr/bin/env python3

import pandas as pd

def split_date(df):
    d = df.str.split(expand=True)
    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    d["Hour"] = d["Hour"].str.split(":", expand=True)[0]

    weekday_map = dict(zip("ma ti ke to pe la su".split(), "Mon Tue Wed Thu Fri Sat Sun".split()))
    month_map = dict(zip("tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu".split(), range(1,13)))

    d["Weekday"] = d["Weekday"].map(weekday_map)
    d["Month"] = d["Month"].map(month_map)

    d = d.astype({"Day": int, "Month": int, "Year": int, "Hour": int})
    return d

def split_date_continues():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df.dropna(axis=0, inplace=True, how="all")
    df.dropna(axis=1, inplace=True, how="all")

    date_df = df.iloc[:, 0]
    rest_df = df.iloc[:, 1:]

    date_df = split_date(date_df)
    cycling_df = pd.concat([date_df, rest_df], axis=1)

    return cycling_df


def bicycle_timeseries():
    bicycle_df = split_date_continues()
    bicycle_df["DateTime"] = pd.to_datetime(bicycle_df[["Year", "Month", "Day", "Hour"]])
    bicycle_df.drop(["Weekday", "Year", "Month", "Day", "Hour"], axis=1, inplace=True)
    bicycle_df.set_index("DateTime", inplace=True)

    return bicycle_df

def main():
    df = bicycle_timeseries()
    print("Shape:", df.shape)
    print("Column names:\n", df.columns)
    print(df.head())

if __name__ == "__main__":
    main()
