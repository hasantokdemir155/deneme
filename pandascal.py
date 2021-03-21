import pandas as pd
import sqlite3
import matplotlib

cnc = sqlite3.connect('emlak.db')
veri= pd.read_sql_query("select * from satlanlar",cnc)
vr=pd.DataFrame(veri)


veri=pd.read_csv('blgkul.csv')

vr= pd.DataFrame(veri)

ksl=vr['LOCATION']=='TUR'
vrtur=vr.loc[ksl,['Value','LOCATION','TIME']]

print(type(vrtur))
print(pd.DataFrame(vrtur))
#vr.columns
print(cm[['TIME','Value']])
#sonc=['LOCATION']
#sonc= vr['Value'].mean()
#sonc1=vr.groupby('LOCATION')['Value'] .['TUR']
#print(sonc1)


#for Value in sonc1:
#    print(Value)
