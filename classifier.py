# all imports
from sklearn import svm,cross_validation
from sklearn.metrics import accuracy_score
from time import time
import numpy as np
import pandas as pd

#read all files
#df1 = pd.read_csv("trainfeature.csv", header = 0)
#df2 = pd.read_csv("trainlabel.csv", header = 0)
#df3 = pd.read_csv("testfeature.csv", header = 0)
#df4 = pd.read_csv("testlabel.csv", header = 0)
df = pd.read_csv("test.csv", header = 0)

X = np.array(df.drop(['Diagnosis of AKI(acute kidney injury)(1-infection,2-rejection,4-Normal subjects,3tac toxicity)'],1))
y = np.array(df['Diagnosis of AKI(acute kidney injury)(1-infection,2-rejection,4-Normal subjects,3tac toxicity)'])
#convert to numpy array
#features_train = df1.as_matrix()
#labels_train = df2.as_matrix()
#features_test = df3.as_matrix()
#labels_test = df4.as_matrix()

X_train , X_test , y_train , y_test = cross_validation.train_test_split(X,y,test_size=0.2)

print (y_train)
#Input style A
# the classifier
#clf = svm.SVC()

# train
#t0 = time()
#clf.fit(features_train, labels_train.ravel())
#print "\ntraining time:", round(time()-t0, 3), "s"

# predict
#t0 = time()
#pred = clf.predict(features_test)
#print "predicting time:", round(time()-t0, 3), "s"

#accuracy = accuracy_score(pred, labels_test.ravel())

#print '\naccuracy = {0}'.format(accuracy)


#Input style B
# the classifier
clf1 = svm.SVC(kernel="rbf")

# train
t1 = time()
clf1.fit(X_train, y_train)
print "\ntraining time:", round(time()-t1, 3), "s"

# predict
t1 = time()
pred = clf1.predict(X_test)
print "predicting time:", round(time()-t1, 3), "s"

accuracy = accuracy_score(pred, y_test)

print '\naccuracy = {0}'.format(accuracy)
