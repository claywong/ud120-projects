#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time

sys.path.append("../tools/")
from email_preprocess import preprocess

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###
'''
from sklearn.naive_bayes import GaussianNB
t0 = time()
clf = GaussianNB()
clf.fit(features_train, labels_train)
#print clf.predict(features_test)
print clf.score(features_test, labels_test)
print "training time:", round(time()-t0, 3), "s"
'''
#########################################################
import numpy
from sklearn.svm import SVC
from sklearn.grid_search import GridSearchCV

features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]

t0 = time()
clf = SVC(kernel='rbf', C=10000)
clf.fit(features_train, labels_train)
predictions = clf.predict(features_test)
score = clf.score(features_test, labels_test)
print "training time:", round(time() - t0, 3), "s"




grid = GridSearchCV(clf, {'kernel': ['linear', 'rbf'], 'C': [1, 10, 100, 1000, 10000]}, 'accuracy')
grid.fit(features_train, labels_train)
best_params = grid.best_params_
model = grid.best_estimator_
score = grid.best_score_

print best_params, model, score

print numpy.count_nonzero(predictions)