#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print enron_data['SKILLING JEFFREY K']
print enron_data['FASTOW ANDREW S']
print enron_data['LAY KENNETH L']

total = 0
total1 = 0

for data in enron_data:
    if enron_data[data]['salary'] != 'NaN':
        print enron_data[data]
        total = total + 1
    if enron_data[data]['email_address'] != 'NaN':
        total1 = total1 + 1

print total
print total1

