#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
del data_dict['TOTAL']
'''
del data_dict['LAY KENNETH L']
del data_dict['SKILLING JEFFREY K']
del data_dict['LAVORATO JOHN J']
del data_dict['BELDEN TIMOTHY N']
del data_dict['FREVERT MARK A']
'''

for key in data_dict:
    if data_dict[key]['salary'] == 'NaN' or data_dict[key]['bonus'] == 'NaN':
        continue
    if data_dict[key]['salary'] > 1000000 or data_dict[key]['bonus'] > 5000000 :
        print key
data = featureFormat(data_dict, features)



### your code below



for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()