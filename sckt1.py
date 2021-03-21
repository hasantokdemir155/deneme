import numpy as np
from sklearn import linear_model
import pandas as pd
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.model_selection import ShuffleSplit
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import cross_validate

import matplotlib.pyplot as plt

#pc=pd.read_csv('cities.csv',usecols=['LatM','LatD','LatS','LonD'],squeeze=True,encoding='utf-8')

pc=pd.read_csv('dn1.csv')

print(pc)


plt.scatter(pc['m'],pc['n'],pc['s'])
plt.show()

x1=pc.iloc[:, 0:-1]
y1=pc.iloc[:, -1]




#x1=pc.drop(["LonD"],axis=1)
#y1=pc["LonD"]

x1_train,x1_test,y1_train,y1_test=train_test_split(x1,y1,train_size=0.8,test_size=0.2,shuffle=True,random_state=64)

#mdl=KNeighborsRegressor()

#mdlx=mdl.fit(x1,y1)
mlp=MLPRegressor()
mlp.fit(x1_train,y1_train)
ver1=mlp.predict(x1)

mdlx=cross_validate(mlp,x1_train,y1_train,cv=4,n_jobs=-1,return_train_score=True)
#mdl.fit(x1_train,y1_train)
#ver=mdl.predict(x1_train)

print(mdlx["test_score"])


print(ver1)

print(mlp.score(x1_train,y1_train))
