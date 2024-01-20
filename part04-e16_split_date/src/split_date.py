#!/usr/bin/env python3

import pandas as pd
import numpy as np


def split_date():
    # days = dict(zip("ma ti ke to pe la su".split(), "Mon Tue Wed Thu Fri Sat Sun".split()))

    # months = dict(zip("tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu".split(), range(1,13)))

    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", usecols=["Päivämäärä"], sep=";")
    df.dropna(inplace=True)

    df = df["Päivämäärä"].str.split(expand=True)
    df.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    df["Hour"] = df["Hour"].str.split(":", expand=True)[0]

    weekday_map = {"ma": "Mon", "ti": "Tue", "ke": "Wed", "to": "Thu", "pe": "Fri", "la": "Sat", "su": "Sun"}
    df["Weekday"] = df["Weekday"].map(weekday_map)

    month_map = {"tammi": 1, "helmi": 2, "maalis": 3, "huhti": 4, "touko": 5, "kesä": 6, "heinä": 7, "elo": 8, "syys": 9, "loka": 10, "marras": 11, "joulu": 12}
    df["Month"] = df["Month"].map(month_map)

    df = df.astype({"Day": int, "Month": int, "Year": int, "Hour": int})


    return df

def main():
    df = split_date()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)
       
if __name__ == "__main__":
    main()
