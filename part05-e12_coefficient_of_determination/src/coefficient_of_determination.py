#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model
import numpy as np

def coefficient_of_determination():
    df = pd.read_csv("src/mystery_data.tsv", sep="\t")
    x = df.iloc[:, :-1]
    Y = df.iloc[:, -1]

    model_linear = linear_model.LinearRegression(fit_intercept=True)
    r2score_X = model_linear.fit(x, Y).score(x, Y)
    X1 = x["X1"].to_numpy()[:, np.newaxis]
    r2score_X1 = model_linear.fit(X1, Y).score(X1, Y)
    X2 = x["X2"].to_numpy()[:, np.newaxis]
    r2score_X2 = model_linear.fit(X2, Y).score(X2, Y)
    X3 = x["X3"].to_numpy()[:, np.newaxis]
    r2score_X3 = model_linear.fit(X3, Y).score(X3, Y)
    X4 = x["X4"].to_numpy()[:, np.newaxis]
    r2score_X4 = model_linear.fit(X4, Y).score(X4, Y)
    X5 = x["X5"].to_numpy()[:, np.newaxis]
    r2score_X5 = model_linear.fit(X5, Y).score(X5, Y)

    return [r2score_X, r2score_X1, r2score_X2, r2score_X3, r2score_X4, r2score_X5]
    
def main():
    r2scores = coefficient_of_determination()
    print(f"R2-score with feature(s) X: {r2scores[0]}")
    for i in range(1, len(r2scores)):
        print(f"R2-score with feature(s) X{i}: {r2scores[i]}")

if __name__ == "__main__":
    main()
