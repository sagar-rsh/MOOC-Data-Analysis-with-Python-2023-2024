#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression

def mystery_data():
    df = pd.read_csv("src/mystery_data.tsv", sep="\t")
    x = df.iloc[:, :-1]
    Y = df.iloc[:, -1]

    model_linear = LinearRegression(fit_intercept=False)
    model_linear.fit(x, Y)

    return model_linear.coef_

def main():
    coefficients = mystery_data()
    # print the coefficients here
    print(f"Coefficient of X1 is {coefficients[0]}")
    print(f"Coefficient of X2 is {coefficients[1]}")
    print(f"Coefficient of X3 is {coefficients[2]}")
    print(f"Coefficient of X4 is {coefficients[3]}")
    print(f"Coefficient of X5 is {coefficients[4]}")

if __name__ == "__main__":
    main()
