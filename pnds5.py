from tkinter import *
from tkinter import ttk
import pandas as pd
from datetime import datetime as dt

import time


cariekr=Tk()
cariekr.geometry("900x900")

lstx2=ttk.Treeview(cariekr,height="60")
    
ttk.Style().theme_use("clam")    
ttk.Style().configure('Treeview',background='silver',foreground='green',fieldbackground="silver")
ttk.Style().map('Treeview',background=[('selected','green')])

#magic041.cs
veri3=pd.read_csv('air.csv',sep=';')
#print(veri3)

vr3=pd.DataFrame(veri3)

#vr3['year'] = pd.DatetimeIndex(vr3['Date']).year

sonc=vr3.groupby('Date').mean()

vrx=vr3['AH'].mean()

print(vrx)
input()

g=[]


#print(sonc)
#input()
#for i in vrx:
#    m=i.split('/')
    
#    g.append(m)
#print(g)


#for i in vrx:
    
#    vr3['Date']=dt.strptime(i,'%d/%m/%Y')      
    #trh=dt.strptime(i,'%d/%m/%Y')
    #print(trh)
#    print(vr3['Date'])
    


#print(type(vr3['Date']))
#print(vr3['Date'])
vr3['year'] = pd.DatetimeIndex(vr3['Date']).year
vr3['month_year'] = pd.to_datetime(vr3['Date']).dt.to_period('M')
sonc=vr3.groupby('year').mean()
sonc1=vr3.groupby('month_year').mean()

print(sonc)
print(sonc1)
#print(vr3['year'])
#s = pd.Series(g)

#s = s.astype(int)

#print(type(s))

#vr3=vr3.assign(pd.DataFrame(g))
#vr3.drop('')

s=vr3.shape

cm=[]
vm=[[]]
#vr3=vr3[5:175]
#print()

tr= vr3.columns
#print(tr[4])
z=len(tr)
for i in range(0,z,1):
    print(i)
       #print(vr3[tr[i]])
    vm.append(vr3[tr[i]].to_list())
   # print(vm)


input()

lstx2["columns"]=vr3.columns
lstx2.column("#0",width = 1)

for m in lstx2["columns"]:
       lstx2.column(m,width=65)
       lstx2.heading(m,text=m)

c=[]


for k in range(1,s[0],1):  
    

    for i in range(1,z+1,1):

    
        a=vm[i][k]               
        c.append(a)
        
    lstx2.insert('',"end",text='',values=(c))   
    c=[]    

a=[]
        
lstx2.pack()
halt

vrx=vr3[["age","workclass","fnlwgt"]]

vm=vrx[10:45]
vm1=vm['age']
vm11=vm['workclass']
vm22=vm['fnlwgt']

s=vm1[3:25]
s11=vm11[3:25]
s22=vm22[3:25]


print(s)
