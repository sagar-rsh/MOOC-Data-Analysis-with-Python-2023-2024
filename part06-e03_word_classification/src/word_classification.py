#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection
from sklearn.feature_extraction.text import CountVectorizer

alphabet="abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = list(alphabet)

# Returns a list of Finnish words
def load_finnish():
    finnish_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename="src/kotus-sanalista_v1.xml"
    load_from_net=False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines=[]
            for line in data:
                lines.append(line.decode('utf-8'))
        doc="".join(lines)
    else:
        with open(filename, "rb") as data:
            doc=data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))

def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines=map(lambda s: s.rstrip(), data.readlines())
    return lines

def get_features(a):
    vec = CountVectorizer(vocabulary=alphabet_set, analyzer="char")
    features = vec.fit_transform(a)

    return features

def contains_valid_chars(s):
    return all(char in alphabet_set for char in s)

def get_features_and_labels():
    finnish_words = load_finnish()
    valid_finnish_words = list(filter(contains_valid_chars, map(lambda x: x.lower(), finnish_words)))

    filtered_eng_nouns = filter(lambda x: x[0].islower(), load_english())
    valid_eng_words = list(filter(contains_valid_chars, map(lambda x: x.lower(), filtered_eng_nouns)))

    words = np.array(valid_finnish_words + valid_eng_words)
    # print(words.shape)

    feature_matrix = get_features(words)
    # print(feature_matrix[0])
    target = np.concatenate((np.zeros((len(valid_finnish_words),)),
                             np.ones((len(valid_eng_words),))), axis=None)
    
    # print(target, target.shape)

    return feature_matrix, target


def word_classification():
    X, y = get_features_and_labels()
    model = MultinomialNB()

    cross_val_gen = model_selection.KFold(n_splits=5, shuffle=True, random_state=0)
    # scores = cross_val_score(model, X,y, cv= 5)
    scores = cross_val_score(model, X,y, cv= cross_val_gen)

    return scores


def main():
    print("Accuracy scores are:", word_classification())

if __name__ == "__main__":
    main()
