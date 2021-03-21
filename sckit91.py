from tkinter import ttk
import pandas as pd
from sklearn.metrics import r2_score
from sklearn import cluster
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score


class lojstkmodel:
    
    def veral(self,z):
        
        self.veri3=pd.read_csv(z,sep=',')
        #print(veri3)
        self.vr3=pd.DataFrame(self.veri3)
        print(self.vr3)

    def modelkur(self):
        self.lrg=LogisticRegression()
        self.lb= LabelEncoder()
        self.vr3.Class=self.lb.fit_transform(self.vr3.Class)
        print('mmmmm')
        
    def modelcalstr(self):
        
        y=self.vr3['Class']
        x=self.vr3.drop('Class',axis=1)

        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,shuffle=True,random_state=123)

        self.lrg.fit(x_train,y_train)
        print(self.vr3.corr())

        print(self.lrg.predict(x_test))
        m=self.lrg.predict(x_test)
        print(accuracy_score(y_true=y_test,y_pred=m))



#print(r2_score(y_test,m))

cals=lojstkmodel()
z='magic041.csv'
cals.veral(z)
cals.modelkur()
cals.modelcalstr()





halt



vr3=vr3.drop('model',axis=1)

#print(vr3)

vr3.info()





