#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)


import numpy

### it's all yours from here forward!  
labels       = numpy.reshape( numpy.array(labels), (len(labels), 1))
features = numpy.reshape( numpy.array(features), (len(features), 1))

from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(labels, features)
print clf.score(labels, features)