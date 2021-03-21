import numpy as np
from sklearn import linear_model
import pandas as pd

from sklearn.model_selection import train_test_split


from sklearn.model_selection import cross_validate
from sklearn.preprocessing import MinMaxScaler


import matplotlib.pyplot as plt





veri_df=pd.read_csv('ornk.csv')

print(veri_df)

x1=veri_df.iloc[:, 0:-1].head(60)
y1=veri_df.iloc[:, -1].head(60)
kosul=x1['m']< 14
#print(x1.iloc[:,])

x11=x1.loc[kosul,:]
print(x11)
#print(x11.describe(include='all'))
#print(x11[['n']].describe())
#print(x1.isnull())

x11['n']=x11.m.astype(float)

print(x11.n.mean())


#print(x1)
#print(y1.shape)
#y1=np.array(y1)

#y1=y1.reshape(-1,1)

#ft=MinMaxScaler()

#ft.fit(y1)
#y=ft.transform(y1)





