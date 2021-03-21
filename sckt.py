import numpy as np
from sklearn import linear_model
import pandas as pd
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.model_selection import ShuffleSplit
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import cross_validate

import matplotlib.pyplot as plt

veri_df=pd.read_csv('dn1.csv')
print(veri_df)

#plt.scatter(veri_df['m'],veri_df['n'])
#plt.show()

x1=veri_df.drop(["s"],axis=1)
y1=veri_df["s"]


#x1=veri_df.iloc[:, 0:-1]
#y1=veri_df.iloc[:, -1]

#m1=veri_df.iloc[:, 0:-1]
print(x1)






#x1=veri_df[['m']].values
#y1=veri_df[['n']].values


x1_train,x1_test,y1_train,y1_test=train_test_split(x1,y1,train_size=0.8,test_size=0.2,shuffle=True,random_state=64)
print("eğitim:",x1_train)
print("test:",x1_test)

mdl=KNeighborsRegressor()

mdlx=mdl.fit(x1,y1)
print(mdlx.predict(x1))

print(mdlx.score(x1,y1))
yeni=[[9],[19]]
yn=pd.DataFrame(yeni).T




print(mdlx.predict(yn))

#mdl=linear_model.LinearRegression()
#mdlx=cross_validate(mdl,x1_train,y1_train,cv=4,n_jobs=-1,return_train_score=True)
#mdl.fit(x1_train,y1_train)
#ver=mdl.predict(x1_train)

#print(np.mean(mdlx["test_score"]))

#print(veri_df.shape)

#plt.scatter(['x1'],['y1'])
#plt.show()

#print(ver)
#print(mdl.score(x1_test,y1_test))
#print(mdlx)

#print(x1)
#print(x1.shape,y1.shape)
#print(y1)

#mlp=MLPRegressor()
#mlp.fit(x1,y1)
#ver1=mlp.predict(x1)

#print(ver1)
#print(mlp.score(x1,y1))
