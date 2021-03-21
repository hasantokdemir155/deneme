from tkinter import ttk
import pandas as pd
from sklearn.metrics import r2_score
from sklearn import cluster
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt



tp=[[3,4,5,'akım','tekim'],[9,8,7,6,'helim','ses']]


print(tp[1][3])




veri3=pd.read_csv('comp.csv',sep=',')
#print(veri3)
vr3=pd.DataFrame(veri3)

sonc1=vr3.groupby('model')['mmin'].mean()
print(sonc1)



for i in sonc1:
    print(i)


vr3=vr3.drop('vendor',axis=1)
vr3=vr3.drop('model',axis=1)

#print(vr3)

vr3.info()



lnr= LinearRegression()

y=vr3['erp']
x=vr3.drop('erp',axis=1)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,shuffle=True,random_state=123)

lnr.fit(x_train,y_train)

print(lnr.predict(x_test))
m=lnr.predict(x_test)
print(r2_score(y_test,m))

print(vr3.corr()['erp'])

print(vr3.columns)

plt.scatter(vr3['prp'],vr3['erp'])
#plt.scatter(vr3['prp'],vr3['mmin'])

#plt.show()


