import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import cluster
from sklearn.preprocessing import LabelEncoder

class sckitlrn:

    def veroku(self):
        self.veri3=pd.read_csv('wdbc.csv')
    #print(veri3)
        self.vr3=pd.DataFrame(self.veri3)
        #print(self.vr3)
    def veridzlt(self,c):        
        self.vr3.drop(c,axis=1,inplace=True)
       
        self.x1=self.vr3.drop('drm',axis=1)
        
        self.lb= LabelEncoder()
        self.vf= self.vr3
        self.vf.drm=self.lb.fit_transform(self.vf.drm)
        print(self.x1.shape)
    def bosveri(self):
        self.vf[['v7','v8','v17','v18','v27','v28']]=self.vf[['v7','v8','v17','v18','v27','v28']].replace(0,np.NaN)
        self.vf.fillna(self.vf.mean(),inplace=True)        
        #print(self.vf.eq(0).sum())
    def modelbaslt(self,s,m):
        self.vf1=self.vf[s]
        print(self.vf1)
        self.vfx=self.vf1[m]
        self.vf1.drop(m,axis=1,inplace=True)
        self.kmn= cluster.KMeans(n_clusters=2,random_state=42)
        print(self.vf1)
        self.kmn.fit(self.vf1)
        print(self.kmn.labels_)
        print(self.vfx)
        print(accuracy_score(self.vfx,self.kmn.labels_))
    def logstcrg(self,s,m):

        self.vf1=self.vf[s]
        #print(self.vf1)
        self.vfx=self.vf1[m]
        self.vf1.drop(m,axis=1,inplace=True)

        
        #print(self.vfl)
        
        self.mdl=LogisticRegression(random_state=0)
        self.X_train,self.X_test,self.y_train,self.y_test=train_test_split(self.vf,self.vfx,train_size=0.8,test_size=0.2,shuffle=True,random_state=64)
        self.mdl.fit(self.X_train,self.y_train)
        self.prd=self.mdl.predict(self.X_test)
        print(accuracy_score(self.y_test,self.prd))
        
        print('loooooo')
def kmleme():        
    cal  = sckitlrn()
    cal.veroku()
    cal.veridzlt('no')
    cal.bosveri()
    cal.modelbaslt(['drm','v3','v8','v21','v23','v24','v28'],'drm')
    cal.logstcrg(['drm','v3','v8','v21','v23','v24','v28'],'drm')
kmleme()

#print(vr3)
#print(vf)





#print(vf.corr())

#print(vf.eq(0).sum())



#print(vf.isnull().sum())
#print(vf.corr().nlargest(7,'drm').index)




