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

enron_data = pickle.load(open("C:\Users\USER\Desktop\machinelearning\ud120-projects-master/final_project/final_project_dataset.pkl", "r"))

""""""
# number of data points(people) in the dataset
print len(enron_data)

# number of features for each person
for key in enron_data:
    print len(enron_data[key])
    break
""""""
# number of POI (person with "poi" = 1 feature)
count_POI = 0
for user in enron_data:
    if enron_data[user]["poi"] == True: count_POI += 1
print count_POI


""""""
# number of POIs exist
poi_names = open('C:\Users\USER\Desktop\machinelearning\ud120-projects-master\\final_project\poi_names.txt', "r")
fr = poi_names.readlines() #readlines(): each lines become items in fr list
print fr # print all items in fr list
print len(fr[2:]) # number of POIs
poi_names.close()

#enron_data.keys() # print every key in the enron_data list

# What kind of features? (print feature name)
# 1)
for key in enron_data:
    for item in enron_data[key]:
        print item
    break
""""""
#individual questions
print enron_data["PRENTICE JAMES"]["total_stock_value"]
print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
""""""

# Who is paied the most?
lay = enron_data["LAY KENNETH L"]["total_payments"]
skilling = enron_data["SKILLING JEFFREY K"]["total_payments"]
fastow = enron_data["FASTOW ANDREW S"]["total_payments"]
most_money = {"lay":lay, "skilling":skilling, "fastow":fastow}
print most_money
print max(most_money.values())
""""""

# print every feature
for key in enron_data:
    for item in enron_data[key]:
        print item
    break
#enron_data[key].keys() #list.keys() brings all the keys in the list

# count the number of NaN in feature 'salary', 'email'
count_salary = 0
count_email = 0
for user in enron_data:
    if enron_data[user]["salary"] != 'NaN': count_salary += 1
    if enron_data[user]["email_address"] != 'NaN': count_email += 1
print count_salary, count_email

# ???? don't know how to use it yet
import sys
sys.path.append("C:\Users\USER\Desktop\machinelearning\ud120-projects-master/tools/")
from feature_format import featureFormat

# count the nubmer of NaN in 'total_payments'
count_NaN_tp = 0
for key in enron_data:
    if enron_data[key]["total_payments"] == 'NaN': count_NaN_tp +=1
print count_NaN_tp
print float(count_NaN_tp)/len(enron_data.keys()) #or len(enron_data)

# count the nubmer of NaN in 'total_payments' in POI
count_NaN_tp = 0
for key in enron_data:
    if enron_data[key]["total_payments"] == "NaN" and enron_data[key]["poi"] == True:
        count_NaN_tp += 1
print "number of \"NaN\" in poi:", count_NaN_tp
print "number of poi:", count_POI
print "% of \"NaN\" in poi:", float(count_NaN_tp) / count_POI
### not a single person in POI has NaN value in total_payments

print "total number of people in dataset:", len(enron_data)

