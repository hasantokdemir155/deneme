import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import cluster
from sklearn.impute import SimpleImputer


veri = pd.read_csv('hcvdat0.csv')
vr= pd.DataFrame(veri)
#print(vr.columns)
impt= SimpleImputer(missing_values=np.nan,strategy='mean')

x1=vr.drop('Unnamed: 0',axis=1)
x2=x1.drop('Category',axis=1)
x3=x2.drop('Age',axis=1)
x4=x3.drop('Sex',axis=1)
print(x4)
print(x1.isnull().sum())
print(x1.shape)
x4=x4.dropna()
print(x4.shape)

#ys=vr.iloc[:,2:12].values
#impt=impt.fit(ys[:,2:12])
#ys[:,2:12]=impt.transform(ys[:,2:12])
#print(ys.isnull().sum())
i = 1
sonc=[]
for i in range(1,5):
    
    kmn= cluster.KMeans(n_clusters=i,random_state=42)
    kmn.fit(x4)
    i = i +1 
    sonc.append(kmn.inertia_)
    print(kmn.labels_)
plt.plot(range(1,5),sonc)
plt.show()


plt.scatter(vr['Unnamed: 0'],vr['ALB'])
plt.scatter(vr['Unnamed: 0'],vr['ALP'])
plt.scatter(vr['Unnamed: 0'],vr['CHE'])
plt.scatter(vr['Unnamed: 0'],vr['GGT'])

