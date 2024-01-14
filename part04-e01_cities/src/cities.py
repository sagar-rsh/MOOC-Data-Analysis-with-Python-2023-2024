#!/usr/bin/env python3

import pandas as pd

def cities():
    fin_cities_df = pd.DataFrame({
        "Population": [231853, 223027, 201810, 279044, 643272],
        "Total area": [643272, 240.35, 3817.52, 528.03, 715.48]
    }, index=["Tampere", "Vantaa", "Oulu", "Espoo", "Helsinki"])
    
    fin_cities_df.sort_values("Population", ascending=False, inplace=True)

    return fin_cities_df
    
def main():
    print(cities())
    
if __name__ == "__main__":
    main()
