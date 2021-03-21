import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import cluster
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn import cluster
from sklearn.neighbors import KNeighborsClassifier
veri=pd.read_csv('abalone.csv')


vr=pd.DataFrame(veri)
a=[]
#print(vr.corr()['Rings'].sort_values())
vr1=vr.groupby('Rings').mean()
#print(vr1.iloc[:,0])
#print(vr1.groupby('Rings'))
vx=vr1.groupby('Rings')
print(vr['Rings'].value_counts())

vm=vr['Sex'].value_counts()

ksl=(vr['Rings']== 27)  | (vr['Rings']== 1) | (vr['Rings']== 23) | (vr['Rings']== 24)| (vr['Rings']== 25) | (vr['Rings']== 2) | (vr['Rings']== 26) | (vr['Rings']== 29)
#ksl1=vr['Rings']==1

snc=vr.loc[ksl]
#snc1=vr.loc[ksl1]
print(vr.shape)
vr.drop([236,294,313,314,480,501,674,678,719,2108,2201,2209,2305,2334,2335,2436,3149,3280],axis=0,inplace=True)
print(vr.shape)
input()
print(snc)
#print(snc1)
input()
s=[]
for i in vm:
    
    s.append(i)


     

for i in vx:
    
    a.append(i[0])


plt.scatter(a,vr1.iloc[:,0])
plt.scatter(a,vr1.iloc[:,1])
plt.scatter(a,vr1.iloc[:,2])
plt.scatter(a,vr1.iloc[:,3])
plt.scatter(a,vr1.iloc[:,4])
plt.scatter(a,vr1.iloc[:,5])
plt.scatter(a,vr1.iloc[:,6])





#plt.show()

vr=vr.drop('Sex',axis=1)
#vrx=vr.drop(,axis=1)

mdl2=cluster.KMeans(n_clusters=3,random_state=42)
mdl2.fit(vr)
print(mdl2.labels_)
y1=vr['Rings']
x1=vr.drop('Rings',axis=1)





mdl3=KNeighborsClassifier(n_neighbors=28)

x_train,x_test,y_train,y_test=train_test_split(x1,y1,test_size=0.2,random_state=123)
print(x_train)
input()
print(y_train)

mdl3.fit(x_train,y_train)
ysnc=mdl3.predict(x_test)
print(accuracy_score(ysnc,y_test))

#print(vr.isnull().sum())



        	
