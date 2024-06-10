#!/usr/bin/env python3
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def explained_variance():
    df = pd.read_csv(r"src/data.tsv", sep="\t")
    feature_variances = df.var().values

    pca = PCA()
    pca.fit(df)

    ev= pca.explained_variance_

    return feature_variances, ev

def main():
    v, ev = explained_variance()

    print(f"The variances are: {' '.join(map(lambda x: format(x, '.3f'), v))}")
    print(f"The explained variances after PCA are: {' '.join(map(lambda x: format(x, '.3f'), ev))}")

    print(sum(v), sum(ev))
    plt.plot(np.arange(1, 11), np.cumsum(ev))
    plt.show()

if __name__ == "__main__":
    main()
