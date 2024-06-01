#!/usr/bin/env python3

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn import metrics

def plant_classification():
    iris = load_iris()
    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, train_size=0.8)
    model = naive_bayes.GaussianNB()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print(y_test, y_pred, sep="\n")
    return metrics.accuracy_score(y_test, y_pred)

def main():
    print(f"Accuracy is {plant_classification()}")

if __name__ == "__main__":
    main()
