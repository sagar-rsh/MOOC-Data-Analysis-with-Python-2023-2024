#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    mask = df["m"] == 7

    return df.loc[mask, "Air temperature (degC)"].mean()

def main():
    print(f"Average temperature in July: {average_temperature()}")

if __name__ == "__main__":
    main()
