import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import accuracy_score

veri=pd.read_csv('maaslar_yeni.csv')
ver=pd.DataFrame(veri)

print(ver.columns)


ver=ver.drop(['Calisan ID','unvan'],axis=1)
#print(ver)
x1=ver.iloc[:, 0:-1]
y1=ver.iloc[:, -1]

a1=ver.iloc[0:10,0:1]
b1=ver.iloc[0:10,-1]


plt.plot(a1,b1)
plt.show()
poly_reg= PolynomialFeatures(degree=2)

a1_pl= poly_reg.fit_transform(a1)
x_train,x_test,y_train,y_test=train_test_split(a1_pl,b1,test_size=0.12,random_state=0)
sc = StandardScaler()


#x_train=sc.fit_transform(x_train)
#x_test=sc.fit_transform(x_test)

#print(x_train)

lr=LinearRegression()

lr.fit(x1,y1)

b1_pred=lr.predict(x1)


#print(accuracy_score(y_true=y1,y_pred=b1_pred))


print(b1_pred)

