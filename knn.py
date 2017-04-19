from __future__ import division
import numpy as np 
from sklearn import neighbors

def knn(features_train, labels_train, features_test):
    X = features_train
    Y = labels_train
    Z = features_test
    
    knn = neighbors.KNeighborsClassifier()
    knn.fit(X,Y)
    z = knn.predict(Z)
    
    return z

def knn_val(features_train, labels_train, features_val, labels_val):
    W = features_train
    X = labels_train
    Y = features_val
    Z = labels_val
    z = 0
    sumCorrect = 0
    
    knn = neighbors.KNeighborsClassifier()
    knn.fit(W, X)
    b = knn.predict(Y)
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
    
        
    
