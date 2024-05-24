#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

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

def cycling_weather():
    weather_df = pd.read_csv("src/kumpula-weather-2017.csv")
    cycling_df = split_date_continues()

    cycling_df[cycling_df["Year"] == 2017]
    cycling_df = cycling_df.groupby(["Year", "Month", "Day"]).sum().reset_index()

    # print(cycling_df)
    res_df = pd.merge(cycling_df, weather_df, left_on=["Year", "Month", "Day"], right_on=["Year", "m", "d"]).drop(["m", "d", "Time", "Time zone"], axis=1)

    return res_df.ffill()


def cycling_weather_continues(station):
    df = cycling_weather()
    x = df.loc[:, ["Precipitation amount (mm)", "Snow depth (cm)", "Air temperature (degC)"]]
    y = df[station]

    model = LinearRegression(fit_intercept=True)
    model.fit(x, y)
    print(model.coef_)
    return (model.coef_, model.score(x, y))
    
def main():
    station = "Merikannontie"
    coefs, r2score = cycling_weather_continues(station)
    print(f"Measuring station: {station}")
    print(f"Regression coefficient for variable 'precipitation': {coefs[0]:.1f}")
    print(f"Regression coefficient for variable 'snow depth': {coefs[1]:.1f}")
    print(f"Regression coefficient for variable 'temperature': {coefs[2]:.1f}")
    print(f"Score: {r2score:.2f}")

if __name__ == "__main__":
    main()
