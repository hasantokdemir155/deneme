import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import cluster
from sklearn.preprocessing import LabelEncoder

veri3=pd.read_csv('wdbc.csv')
#print(veri3)
vr3=pd.DataFrame(veri3)

vr3.drop('no',axis=1,inplace=True)
#print(vr3)
#print(vf)
x1=vr3.drop('drm',axis=1)

lb= LabelEncoder()
vf= vr3
vf.drm=lb.fit_transform(vf.drm)


print(vr3)
#print(vf.corr())

print(vf.eq(0).sum())

vf[['v7','v8','v17','v18','v27','v28']]=vf[['v7','v8','v17','v18','v27','v28']].replace(0,np.NaN)
print(vf.eq(0).sum())
vf.fillna(vf.mean(),inplace=True)

print(vf.isnull().sum())
print(vf.corr().nlargest(7,'drm').index)

vf1=vf[['drm','v3','v8','v21','v23','v24','v28']]
print(vf1)
vfx=vf1['drm']
vf1.drop('drm',axis=1,inplace=True)
kmn= cluster.KMeans(n_clusters=2,random_state=42)
print(vf1)
kmn.fit(vf1)
print(kmn.labels_)
print(vfx)

print(accuracy_score(vfx,kmn.labels_))

