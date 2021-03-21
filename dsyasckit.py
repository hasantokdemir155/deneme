import numpy as np
from sklearn import linear_model
import pandas as pd
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.model_selection import ShuffleSplit
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import cross_validate
from sklearn.preprocessing import MinMaxScaler


import matplotlib.pyplot as plt



ods=open("ornk.csv",'w+')


ods.write("m"+","+"n"+","+"s"+"\n")
k=0
for i in range (250):
    #with open("ornk.txt","w+") as ods:
      k=k+1
      ods.write(str(i+3)+","+str(i*1.14)+","+str(k+1)+"\n")
      if k == 4:
          k=0  

ods.close()


veri_df=pd.read_csv('ornk.csv')



x1=veri_df.iloc[:, 0:-1].head(60)
y1=veri_df.iloc[:, -1].head(60)

print(x1)
print(y1.shape)
#y1=np.array(y1)

#y1=y1.reshape(-1,1)

#ft=MinMaxScaler()

#ft.fit(y1)
#y=ft.transform(y1)





print(y1)


mdl=KNeighborsRegressor()
#mdl=linear_model.LinearRegression()
#mdlx=cross_validate(mdl,x1_train,y1_train,cv=4,n_jobs=-1,return_train_score=True)
verx=mdl.fit(x1,y1)
print('xxxx')
ver=mdl.predict(x1)
print(verx.score(x1,y1))


#print(y1)

#yn=veri_df.DataFrame(yeni).T
#ver1=mdl.predict(9)
print(ver)
#print(mdlx.predict(yn))



#print(np.mean(mdlx["test_score"]))
