import pandas as pd
import numpy
import matplotlib.pyplot as pyp
pc=pd.read_csv('cities.csv',usecols=['LatM','LatD','LatS','City'],squeeze=True,encoding='utf-8')

#print(pc.sort_values(['LatM']).tail(12))
#print(pc.get([0,1,2,3,4,5,6,7]))
#print(type(pc))
pd_df=pd.DataFrame(pc)
#print(pd_df)
#print(pd_df[   ['LatD','LatM']    ])

#print(pc.loc[[8,5]])

pd_df2=pd.DataFrame(pc,columns=['LatD','LatM','City'],index=[4,9,12,15])
print(pd_df2)

print(pd_df['LatD'][12])

pd_df2['dal']=[7,9,17,45]

print(pd_df2)
#print(pd_df2.describe())
#new_row=pd.DataFrame({'LatD':'14','LatM':'38'},index=['hayırlı'])
#pd_df2=pd_df2.append(new_row)
#print(pd_df2)

#pd_df2.pop('dal')
#print(pd_dfprint(2)

#print(pd_df2.drop([[4,12]],axis=0))

#print(pd_df2.iloc[[0]])

#print(pd_df2[['dal'][0:3]])

#for sra ,satr in pd_df2.iterrows():
#    print(sra)
#    print(satr)

#print(pd_df['City'].describe())
#array(['Wilmington'],dtype=object)
#print(pd_df['City'].unique())
#print(pd_df['City'][14])      
#veritksl=pd_df2['dal'] >= 17 
#veritksl=pd_df['City'].str.contains('Wilmington')
#print(pd_df['City'].str.contains('Wilmington').loc[:])
#print(veritksl) 
#print(pd_df.loc[veritksl,:])#.head(1))
##print()

##print((pd_df[(pd_df.LatD> 30) & (pd_df.LatD < 98) & (pd_df['City'].str.contains('Wilmington'))].tail(1)))

#print(pd_df[['LatM']].add(5).head())

##pd_df.sort_values('City',inplace=True)
print('xxxx')
grf=pd_df['City']=='Wilmington'
print(grf)

#print(pd_df[['City','LatD']].tail(10))
#print(pd_df['City'].unique())
pyp.scatter(grf['City'][0:3],grf['LatD'][0:3])
pyp.show()
