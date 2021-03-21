from tkinter import ttk
import pandas as pd
from sklearn.metrics import r2_score
from sklearn import cluster
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score


veri3=pd.read_csv('magic041.csv',sep=',')
#print(veri3)
vr3=pd.DataFrame(veri3)
print(vr3)

lrg=LogisticRegression()
lb= LabelEncoder()
vr3.Class=lb.fit_transform(vr3.Class)


print(vr3.corr())


y=vr3['Class']
x=vr3.drop('Class',axis=1)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,shuffle=True,random_state=123)

lrg.fit(x_train,y_train)

print(lrg.predict(x_test))
m=lrg.predict(x_test)
print(accuracy_score(y_true=y_test,y_pred=m))
#print(r2_score(y_test,m))

halt



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


