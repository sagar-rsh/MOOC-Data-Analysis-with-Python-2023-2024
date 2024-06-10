#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances

from matplotlib import pyplot as plt

import seaborn as sns
sns.set(color_codes=True)
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc
import scipy


nucleotide_mapping = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
def toint(x):
    return nucleotide_mapping[x]

def get_features_and_labels(filename):
    df = pd.read_csv(filename, sep="\t")

    X = df['X'].apply(lambda x: list(map(toint, list(x))))
    y = df.y

    return (np.stack(X), np.stack(y))

def plot(distances, method='average', affinity='euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage )
    g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} affinity")
    plt.show()

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def cluster_euclidean(filename):
    X, y = get_features_and_labels(filename)
    model = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='average', compute_distances=True) #by default metric is set to euclidean
    pred_y = model.fit_predict(X)

    permutation = find_permutation(2, y, pred_y)
    new_lables = [permutation[label] for label in pred_y]

    return accuracy_score(y, new_lables)

def cluster_hamming(filename):
    X, y = get_features_and_labels(filename)
    D = pairwise_distances(X, metric='hamming')
    model = AgglomerativeClustering(n_clusters=2, affinity='precomputed', linkage='average') 
    pred_y = model.fit_predict(D)

    # plot(D, method='average', affinity='hamming')

    permutation = find_permutation(2, y, pred_y)
    new_lables = [permutation[label] for label in pred_y]

    return accuracy_score(y, new_lables)

def main():
    print("Accuracy score with Euclidean affinity is", cluster_euclidean("src/data.seq"))
    print("Accuracy score with Hamming affinity is", cluster_hamming("src/data.seq"))

if __name__ == "__main__":
    main()
