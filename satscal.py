import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
veri2=pd.read_csv('sats.csv')
print(veri2)
vr=pd.DataFrame(veri2)    
x1=vr[['Aylar']]
y1=vr[['Satislar']]

x_train,x_test,y_train,y_test=train_test_split(x1,y1,test_size=0.12,random_state=0)
sc = StandardScaler()

x_train=sc.fit_transform(x_train)
x_test=sc.fit_transform(x_test)
print(x_train,x_test)
