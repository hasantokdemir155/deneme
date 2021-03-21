import numpy as np
#from sklearn import datasets,svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score
from sklearn import cluster
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import PCA



veri3=pd.read_csv('wdbc.csv')
#print(veri3)
vr3=pd.DataFrame(veri3)

#mdl=PCA()






#print(vr3.drm8).value_counts())
print(vr3.corr())
input()
lb= LabelEncoder()
vf= vr3
vf.drm=lb.fit_transform(vf.drm)

#print(vf.drm)

#print(onehot_df)



vf.drop('no',axis=1,inplace=True)
#print(vr3)
#print(vf)


print(vf.corr()['drm'].sort_values())
print('')
input()


x1=vf.drop('drm',axis=1)
y1=vf['drm']

#print(y1)
#print(x1)
pca = PCA()
print(pca.explained_variance_ratio)



mdl=LogisticRegression(random_state=0)
mdl2=cluster.KMeans(n_clusters=2,random_state=42)
mdl2.fit(x1)
#print('şşşşş')
#print(mdl2.cluster_centers_.round(2))
X_train,X_test,y_train,y_test=train_test_split(x1,y1,train_size=0.8,test_size=0.2,shuffle=True,random_state=42)

x_train2= pca.fit_transform(X_train)

#print(x_train2)
#input()

mdlx=LogisticRegression(random_state=0)
snc=mdlx.fit(x_train2,y_train)
sncx=mdlx.predict(x_train2)

snc=mdl.fit(X_train,y_train)
sncx1=mdl.predict(X_train)
#print(confusion_matrix(y_train,sncx))
#print(confusion_matrix(y_train,sncx1))
#input()
#print(mdl2.labels_)
#print(y_train)
mdl.fit(X_train,y_train)
parm={'n_cluster':[2,3]}

grid=GridSearchCV(mdl2,parm,cv=5)
grid.fit(x1,y1)
print(grid.score)

yth=mdl.predict(X_test)

print(confusion_matrix(y_true=y_test,y_pred=yth))

print(accuracy_score(y_true=y_test,y_pred=yth))
print(accuracy_score(y1,mdl2.labels_ ))
plt.scatter(x1[:,0],x1[:,1],c=mdl2.labels_)
plt.show()
