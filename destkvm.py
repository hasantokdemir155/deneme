import numpy as np
from sklearn import datasets,svm
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
import pandas as pd


veri= datasets.load_digits()
vr=veri.data
m=veri.target
print(veri.target.shape)
plt.matshow(veri.images[0])


X_train,X_test,y_train,y_test= train_test_split(vr,m,test_size=0.25,random_state=65)

print(X_train.shape,y_train.shape,y_test.shape,X_test.shape)
print(y_test.shape)

mdl=svm.SVC()


mdl.fit(X_train,y_train)
y_predict=mdl.predict(X_test)
print(y_predict.shape,y_train.shape)

print(accuracy_score(y_test,y_predict))
#print(clasification_report(y_test,y_predict))
print(vr)
