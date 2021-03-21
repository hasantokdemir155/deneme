import numpy as np
import pandas as pd

class pand:
    def dosyaal(self):
        self.veri2=pd.read_csv('eksikveriler.csv')
        print(veri2)
        self.vr=pd.DataFrame(veri2)    

cr = pand()
cr.dosyaal
#veri2=pd.read_csv('eksikveriler.csv')

#print(veri2)

#print(veri2.columns)

#vr=pd.DataFrame(veri2)
#print(vr)

print(cr.vr.isnull)

from sklearn.impute import SimpleImputer

impt= SimpleImputer(missing_values=np.nan,strategy='mean')

ys =vr.iloc[:,1:4].values
impt= impt.fit(ys[:,1:4])

ys[:,1:4]=impt.transform(ys[:,1:4])
print(ys)

from sklearn import preprocessing

lenk= preprocessing.LabelEncoder()

ulk= vr.iloc[:,0:1].values
ulk[:,0] = lenk.fit_transform(vr.iloc[:,0])

#print(ulk)

oneht= preprocessing.OneHotEncoder()
ulk= oneht.fit_transform(ulk).toarray()
print(ulk)
print(ys)
ulksnc= pd.DataFrame(data=ys,index=range(22),columns=['boy','kilo','yas'])
klo = vr.iloc[:,2:3].values
by = vr.iloc[:,1:2].values
sn1=pd.DataFrame(data=klo,index=range(22),columns=['kilo'])
sn2=pd.DataFrame(data=by,index=range(22),columns=['boy'])

s=pd.concat([sn1,sn2],axis=1)


print(s)
