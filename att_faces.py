import sys

import tarfile
import numpy as np

tar = tarfile.open("C:\Users\USER\Desktop\machinelearning/att_faces.tar","r")

for member in tar.getmembers():
     f = tar.extractfile(member)
     if f is not None:
         content = f.read()
#         Data = np.loadtxt(content)



"""
print("Fitting the classifier to the training set")
t0 = time()
param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5],
              'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1], }
clf = GridSearchCV(SVC(kernel='rbf', class_weight='balanced'), param_grid)
clf = clf.fit(X_train_pca, y_train)
print("done in %0.3fs" % (time() - t0))
print("Best estimator found by grid search:")
print(clf.best_estimator_)
"""