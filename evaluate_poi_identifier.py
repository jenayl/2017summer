#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here
from sklearn import model_selection
features_train, features_test, labels_train, labels_test = model_selection.train_test_split(features, labels, test_size=0.3, random_state=42)

from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
poi_test = len([e for e in pred if e==1])
total_test = len(features_test)
print clf.score(features_test, labels_test)
print "number of POI in test set: ", poi_test
print "total number of test set", total_test
print "Accuracy: ", float(total_test-poi_test)/total_test

# compare prediction and labels_test: no true positive(TP) found
print pred
import numpy as np
np_test = np.array(labels_test)
print np_test

# instead of accuracy, let's use precision and recall
from sklearn.metrics import precision_score, recall_score
print "precision", precision_score(labels_test, pred)
print "recall", recall_score(labels_test, pred)

# calculate precision and recall by hand (using tp,np,fp)
predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

confusion = zip(predictions, true_labels)
tp = 0
tn = 0
fp = 0
for i in confusion:
    if i[0]==i[1]==1: tp += 1
    elif i[0]==i[1]==0: tn += 1
    elif i[0]==1 and i[1]==0: fp += 1
fn = len(confusion)-(tp+tn+fp)
print "True Positives", tp
print "True Negatives", tn
print "False Positives", fp
print "False Negatives", fn

precision  = float(tp)/(tp+fp)
print "Precision", precision
recall = float(tp)/(tp+fn)
print "Recall", recall

# f1_score is the trade-off b/w precision and recall
# higher f1_score, the better :D
from sklearn.metrics import f1_score
print f1_score(true_labels, predictions)