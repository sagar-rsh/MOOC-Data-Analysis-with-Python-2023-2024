#!/usr/bin/env python3

import scipy.stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    iris_data = load()
    sepal_len, petal_len = iris_data[:, 0], iris_data[:, 2]
    return scipy.stats.pearsonr(sepal_len, petal_len)[0]

def correlations():
    iris_data = load()
    return np.corrcoef([iris_data[:, 0], iris_data[:, 1], iris_data[:, 2], iris_data[:, 3]])

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
