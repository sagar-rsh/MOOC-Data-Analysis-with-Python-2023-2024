#!/usr/bin/env python3
import gzip
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

def read_compressed_files(path, fraction):
    file =  gzip.open(rf"{path}", 'rb')
    data = file.readlines()
    # print(len(data))
    lines_to_read = round(len(data) * fraction)

    return data[: lines_to_read]

def get_features(a):
    vec = CountVectorizer()
    features = vec.fit_transform(a)

    return features.toarray()

def get_features_and_labels(ham_data, spam_data):
    data = np.array(ham_data + spam_data)
    # print(data[0])
    features = get_features(data)
    labels = np.concatenate((np.zeros(len(ham_data)), np.ones(len(spam_data))), axis = None)
    # print(features.shape)
    # print(labels.shape)

    return features, labels

def spam_detection(random_state=0, fraction=1.0):
    ham_data = list(read_compressed_files(r"src/ham.txt.gz", fraction))
    spam_data = list(read_compressed_files(r"src/spam.txt.gz", fraction))

    X, y = get_features_and_labels(ham_data, spam_data)
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75, random_state=random_state)

    model = MultinomialNB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    score = metrics.accuracy_score(y_test, y_pred)

    miscallified = sum(map(lambda x,y: bool(x-y),y_test,y_pred))
    # print(miscallified)
    return score, X_test.shape[0], miscallified

def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages misclassified out of {total}")

if __name__ == "__main__":
    main()
