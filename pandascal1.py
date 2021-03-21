import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk




cariekr=Tk()
cariekr.geometry("500x500")

lstx2=ttk.Treeview(cariekr,height="21")
    
ttk.Style().theme_use("clam")    
ttk.Style().configure('Treeview',background='silver',foreground='green',fieldbackground="silver")
ttk.Style().map('Treeview',background=[('selected','green')])



cnc = sqlite3.connect('emlak.db')
veri= pd.read_sql_query("select * from satlanlar",cnc)
vr=pd.DataFrame(veri)




veri=pd.read_csv('unemply.csv')

vr= pd.DataFrame(veri,columns=['LOCATION','TIME','Value'])
#print(vr.head(20))

ksl=vr['LOCATION']=='AUS'
vrtur=vr.loc[ksl,['Value','LOCATION','TIME']].head(50)

x1=vrtur['TIME']
y1=vrtur['Value']

sonc= vrtur['Value'].mean()
sonc1=vr.groupby('LOCATION')['Value'].mean()
sonc2=vr.groupby('TIME')['Value'].mean()

sonc3=vr.groupby('TIME')
print(sonc3.head(2))
input()
for i,group   in sonc3:
      print(i)
      print(group)
    


#print(sonc2.describe())




lstx2["columns"]= ['zaman','oran']
#print(lstx2["columns"])
lstx2.column("#0",width = 2)
for i in sonc2:
    lstx2.insert('',"end",text='',values=(i))



lstx2.pack()

#print(x1,y1)
plt.scatter(x1,y1)
plt.plot(x1,y1)

#plt.show()

ksl=vr['LOCATION']=='TUR'
vrtur=vr.loc[ksl,['Value','LOCATION','TIME']]




#print(type(vrtur))
#print(pd.DataFrame(vrtur))
#vr.columns
#print(cm[['TIME','Value']])
#sonc=['LOCATION']
#sonc= vr['Value'].mean()
#sonc1=vr.groupby('LOCATION')['Value'] .['TUR']
#print(sonc1)


#for Value in sonc1:
#    print(Value)
