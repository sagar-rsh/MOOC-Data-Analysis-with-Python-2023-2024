#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    df = pd.read_csv("src/who_suicide_statistics.csv")
    df["Suicide fraction"] = df["suicides_no"] / df["population"]
    result = df.groupby("country").mean()

    return result["Suicide fraction"]
    
def suicide_weather():
    suicide_fractions_ser = suicide_fractions()
    suicide_fractions_ser.sort_index(inplace=True)

    avg_temp_df = pd.read_html("src/List_of_countries_by_average_yearly_temperature.html", header=0, index_col=0)[0]
    avg_temp_ser = avg_temp_df["Average yearly temperature (1961–1990, degrees Celsius)"]
    avg_temp_ser = avg_temp_ser.str.replace("\u2212", "-").astype(float)
    avg_temp_ser.sort_index(inplace=True)

    common_rows_cnt = avg_temp_ser.index.intersection(suicide_fractions_ser.index).size
    corr = avg_temp_ser.corr(suicide_fractions_ser, method="spearman")
    
    return (suicide_fractions_ser.size, avg_temp_df.size, common_rows_cnt, corr)

def main():
    suicide_df_size, avg_temp_df_size, common_rowcount, corr = suicide_weather()
    print(f"Suicide DataFrame has {suicide_df_size} rows")
    print(f"Temperature DataFrame has {avg_temp_df_size} rows")
    print(f"Common DataFrame has {common_rowcount} rows")
    print(f"Spearman correlation: {corr}")


if __name__ == "__main__":
    main()
