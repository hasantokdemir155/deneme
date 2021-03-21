

import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder


vrm=pd.read_csv('imports-85.csv')

vrm1=pd.DataFrame(vrm)
#print(vrm1)

#print(vrm1.isnull().sum())


vrx=vrm1.drop(['symboling','normalized-losses'],axis=1)
#print(vrx)

vrml=vrx.drop(['length','width','height','curb-weight'],axis=1)

ksl=vrx['num-of-doors']=='?'

sn=vrx.loc[ksl,:]
print(sn)
vrx.drop([27,63],axis=0,inplace=True)


#ksl=(vr['Rings']== 27) 

degskenler=['make','fuel-type','aspiration','num-of-doors','body-style','drive-wheels','engine-location','wheel-base','length','width','height','curb-weight','engine-type']
for i in degskenler:
    ksl=(vrx[i]=='?').sum()
    
    print(ksl)
    input()
    





onh = OneHotEncoder(handle_unknown='ignore')
# passing bridge-types-cat column (label encoded values of bridge_types)

onh_df = pd.DataFrame(onh.fit_transform(vrx[['make']]).toarray())

onh_df.columns=onh.categories_
print(onh_df)

onh_dfx1 = OneHotEncoder(handle_unknown='ignore')

onh_df1=pd.DataFrame(onh_dfx1.fit_transform(vrx[['fuel-type']]).toarray())
onh_df1.columns=onh_dfx1.categories_

onh_dfx2 = OneHotEncoder(handle_unknown='ignore')



onh_df2=pd.DataFrame(onh_dfx2.fit_transform(vrx[['aspiration']]).toarray())

onh_dfx3 = OneHotEncoder(handle_unknown='ignore')

onh_df3=pd.DataFrame(onh_dfx3.fit_transform(vrx[['num-of-doors']]).toarray())

onh_dfx4 = OneHotEncoder(handle_unknown='ignore')


onh_df4=pd.DataFrame(onh_dfx4.fit_transform(vrx[['body-style']]).toarray())

onh_dfx5 = OneHotEncoder(handle_unknown='ignore')


onh_df5=pd.DataFrame(onh_dfx5.fit_transform(vrx[['drive-wheels']]).toarray())

onh_dfx6 = OneHotEncoder(handle_unknown='ignore')

onh_df6=pd.DataFrame(onh_dfx6.fit_transform(vrx[['engine-location']]).toarray())

print(onh_df5.columns)

print(onh_dfx2.categories_,onh_dfx3.categories_,onh_dfx4.categories_,onh_dfx5.categories_)
print(ksl)
