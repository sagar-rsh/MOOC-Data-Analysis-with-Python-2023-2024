#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

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

def bicycle_timeseries():
    bicycle_df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    bicycle_df = bicycle_df.dropna(axis=0, how="all").dropna(axis=1, how="all")
    date_df = split_date(bicycle_df.iloc[: ,0])
    bicycle_df = pd.concat([date_df, bicycle_df.iloc[:, 1:]], axis=1)

    bicycle_df["DateTime"] = pd.to_datetime(bicycle_df[["Year", "Month", "Day", "Hour"]])
    bicycle_df.drop(["Year", "Month", "Day", "Hour"], axis=1, inplace=True)

    return bicycle_df

def commute():
    bicycle_df = bicycle_timeseries()

    mask = ((bicycle_df["DateTime"].dt.year == 2017) & (bicycle_df["DateTime"].dt.month == 8))
    aug_2017 = bicycle_df[mask]

    weekday_map = dict(zip("Mon Tue Wed Thu Fri Sat Sun".split(), range(1,8)))
    aug_2017.loc[:, "Weekday"] = aug_2017.loc[:, "Weekday"].map(weekday_map)

    return aug_2017.groupby("Weekday").sum()
    
def main():
    df = commute()
    print("Shape:", df.shape)
    print("Column names:\n", df.columns)
    print(df.head())

    plt.plot(df)
    plt.legend(df.columns, bbox_to_anchor=(1.05, 1.0), loc='upper left')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
