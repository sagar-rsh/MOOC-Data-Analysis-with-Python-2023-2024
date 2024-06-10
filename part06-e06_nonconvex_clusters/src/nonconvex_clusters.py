#!/usr/bin/env python3

import scipy
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)

    return permutation

def remove_outlier_data(real_labels, labels):
    idx = labels != -1
    new_labels = labels[idx]
    new_real_labels = real_labels[idx]

    return new_real_labels, new_labels

def clustering(X, y, eps):
    model = DBSCAN(eps=eps)
    model.fit(X)

    n_outliers = (model.labels_ == -1).sum()

    y, new_labels = remove_outlier_data(y, model.labels_)
    n_clusters = len(set(new_labels))

    if (n_clusters != y.nunique()):
        return [eps, np.nan, n_clusters, n_outliers]

    permutation = find_permutation(n_clusters, y, new_labels)
    new_labels = [permutation[label] for label in new_labels]    
    score = accuracy_score(y, new_labels)

    return [eps, score, n_clusters, n_outliers]

def nonconvex_clusters():
    df = pd.read_csv(r"src/data.tsv", sep="\t")
    X = df.loc[:, ["X1", "X2"]]
    y = df.y

    cluster_list = []
    for i in np.arange(0.05, 0.2, 0.05):
        cluster_list.append(clustering(X, y, i))

    return pd.DataFrame(cluster_list, columns=["eps", "Score", "Clusters", "Outliers"], dtype=float)

def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()
