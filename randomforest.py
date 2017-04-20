from __future__ import division
import numpy as np
from sklearn import ensemble

def randomforest(features_train, labels_train, features_test):
    X = features_train
    Y = labels_train
    Z = features_test

    randomforest = ensemble.RandomForestClassifier(nest)
    randomforest.fit(X,Y)
    z = randomforest.predict(Z)

    return z

def randomforest_val(features_train, labels_train, features_val, labels_val):
    W = features_train
    X = labels_train
    Y = features_val
    Z = labels_val
    z = 0
    sumCorrect = 0

    randomforest = ensemble.RandomForestClassifier()
    randomforest.fit(W, X)
    b = randomforest.predict(Y)
    y = b.tolist()
    val_len = len(features_val)
    i = 0
    for array in y:
        try:
            temp = array.index(1)
            pass
        except ValueError:
            temp = 9
        if temp == Z[i]:
            sumCorrect = sumCorrect+1
        i = i + 1

    accuracy = sumCorrect/val_len
    print(sumCorrect)
    result = [b]
    print result
    result.append(accuracy)
    return result
