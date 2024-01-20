#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
    df = pd.DataFrame({"State": ["United Kingdom", "Finland", "USA", "Sweden", "Germany", "Russia"], 
                  "Year of independence": ['-', 1917, 1776, 1523, '-', 1992],
                  "President": ["-", "Niinistö", "Trump", "-", "Steinmeier", "Putin"]})
    df.set_index("State", inplace=True)
    df["Year of independence"].replace("-", np.nan, inplace=True)
    df["President"].replace("-", np.nan, inplace=True)

    return df
               
def main():
    print(missing_value_types())

if __name__ == "__main__":
    main()
