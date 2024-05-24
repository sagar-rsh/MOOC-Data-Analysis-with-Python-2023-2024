#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    model = LinearRegression(fit_intercept=True)
    model.fit(x[:, np.newaxis], y)

    return model.coef_[0], model.intercept_
    
def main():
    x = np.linspace(20, 70, 50)
    y = 5*x + 1 * np.random.randn(50)

    slope, intercept = fit_line(x, y)
    print("Slope: ", slope)
    print("Intercept: ", intercept)

    plt.scatter(x, y)
    x1 = np.linspace(0, 100, 10)
    plt.plot(x1, x1*slope + intercept, 'red')

    plt.show()

if __name__ == "__main__":
    main()
