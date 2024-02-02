#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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


def cyclists_per_day():
    df = split_date_continues()
    groups = df.groupby(["Year", "Month", "Day"])

    return groups.sum().drop(["Hour"], axis=1)
    
def main():
    df = cyclists_per_day()
    print("Shape:", df.shape)
    print("Column names:\n", df.columns)
    print(df.head())

    # df = df.loc[(2017, 8), :]
    # df.plot()
    # plt.show()

    aug_2017 = df.groupby(["Year", "Month"]).get_group((2017, 8))
    print(aug_2017)
    plt.plot(np.arange(1, len(aug_2017)+1), aug_2017)
    plt.legend(aug_2017.columns, bbox_to_anchor=(1.05, 1.0), loc='upper left')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
