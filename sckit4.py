import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import cluster
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression


veri=pd.read_csv('forestfires.csv')

vr=pd.DataFrame(veri)
print(vr)
print(vr['temp'].mean())
vr=vr.drop(['month','day','X','Y','wind','area','RH','rain'],axis=1)
print(vr)
a=[]
for i in vr.values:
   # print(i)
    a.append(i[4])
    #input(

y1=vr['FFMC']
x1=vr.drop(['FFMC'],axis=1)

x_train,x_test,y_train,y_test=train_test_split(x1,y1,test_size=0.33,random_state=0)    

print(y_test.eq(0).sum())
input()
mdl=LinearRegression()
cl=mdl.fit(x_train,y_train)
yprd=mdl.predict(x_test)
print(y_test)

print(cl.score(x_test,yprd))



#print(np.mean(a))
#print(vr.corr()['FFMC'])
plt.scatter(vr['FFMC'],vr['temp'])
plt.scatter(vr['FFMC'],vr['DMC'])
plt.scatter(vr['FFMC'],vr['DC'])
plt.scatter(vr['FFMC'],vr['ISI'])
#plt.scatter(vr['FFMC'],vr['RH'])
#plt.scatter(vr['FFMC'],vr['rain'])


#plt.show()

