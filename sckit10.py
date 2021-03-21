import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import cluster
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
veri=pd.read_csv('covtype.csv',sep=',',header=None)
vr=pd.DataFrame(veri,columns=[0,1,2,3,4,5,6,7,8,9,10,54])
sonc=vr.groupby(0).count()

print(sonc)

halt




veri=pd.read_csv('clean1.csv',sep=',',header=None)

#veri=pd.read_csv('clean1.csv',nrows=5,sep=',',header=None)

#veri=pd.read_csv('vercal.csv',sep
#pd.read_csv('dosyaAdi.csv', nrows=7, sep=',')

vr=pd.DataFrame(veri)

#print(vr.iloc([0],[0]))
#vr.loc([5,['1']])

sonc=vr.groupby(0).count()
print(sonc)
halt

for i,m in vr.iterrows():
    print(m[0],m[1],m[2],m[3],m[4],m[5])
    input()





