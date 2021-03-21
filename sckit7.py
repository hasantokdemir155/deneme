import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import cluster
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier

veri=pd.read_csv('adult.csv',sep=', ')
#veri=pd.read_csv('vercal.csv',sep=';')

vr=pd.DataFrame(veri)

vrx=vr.iloc[10:85,4:9]
vrxx=vr['capital-gain'].value_counts()
print(vr.columns)

#for i in vrxx:
#    print(i)

print(vrxx.sum())

print(vrxx)
#print(vr['education'])



##
  #  plt.scatter(a,vr1.iloc[:,0])
   # plt.scatter(a,vr1.iloc[:,1])
   # plt.scatter(a,vr1.iloc[:,2])
   # plt.scatter(a,vr1.iloc[:,3])
   # plt.scatter(a,vr1.iloc[:,4])
   # plt.scatter(a,vr1.iloc[:,5])
   # plt.scatter(a,vr1.iloc[:,6])

#plt.show()
        	
