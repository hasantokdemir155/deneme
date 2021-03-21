import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

class calsma:
     veri=pd.read_csv('iris.csv')
     ver=pd.DataFrame(veri)   
        
     def dosyaal(modeller,x_train,y_train,x_test,y_test):
         md=[]   
         for ism,model in modeller:
    
            #if i =='lg':
                #lg.fit(x_train,y_train)
                clf = model.fit(x_train, y_train)
                cm=confusion_matrix(y_test,clf.predict(x_test))
                #print(ism,cm)
                md.append(cm)
         return(md)    
            #if i =='knn':
        
             #   knn.fit(x_train,y_train)
             #   cm=confusion_matrix(y_test,knn.predict(x_test))
             #   print('knn',cm)
        
            #if i =='dtc':
             #   dtc.fit(x_train,y_train)
             #   cm=confusion_matrix(y_test,dtc.predict(x_test))
             #   print('dtc')
             #   print(cm)
           
            
            
            


orn= calsma
#orn.dosyaal()


x1=orn.ver.iloc[:, 0:-1]
y1=orn.ver.iloc[:, -1]
a1=orn.ver.iloc[:,0:1]
b1=orn.ver.iloc[:,1:2]
c1=orn.ver.iloc[:,2:3]
plt.scatter(a1,b1)
plt.scatter(a1,c1)

plt.show()
#poly_reg= PolynomialFeatures(degree=2)
sc = StandardScaler()
#a1_pl= poly_reg.fit_transform(a1)
x_train,x_test,y_train,y_test=train_test_split(x1,y1,test_size=0.33,random_state=123)
lg=LogisticRegression()
knn=KNeighborsClassifier(n_neighbors=1)
knn.fit(x_train,y_train)
ypd=knn.predict(x_test)
#print(ypd)
dtc=DecisionTreeClassifier()

modeller=[('lg',LogisticRegression()),('knn',KNeighborsClassifier(n_neighbors=1)),('dtc',DecisionTreeClassifier())]

print(orn.dosyaal(modeller,x_train,y_train,x_test,y_test))
        

x_train=sc.fit_transform(x_train)
x_test=sc.fit_transform(x_test)
from sklearn.cluster import KMeans

ntc=[]

for i in range(1,5):
    kmn=KMeans(n_clusters=i,init='k-means++',random_state=123)
    kmn.fit(x_train)
    ntc.append(kmn.inertia_)

    
plt.plot(range(1,5),ntc)
plt.show()



#print(accuracy_score(y_true=y1,y_pred=b1_pred))




