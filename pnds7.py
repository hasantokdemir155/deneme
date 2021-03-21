from tkinter import *
from tkinter import ttk
import pandas as pd
import csv
from datetime import datetime as dt

import time

cariekr=Tk()
cariekr.geometry("900x900")

t='142a'
print(t.replace('a',' '))
print(t)

lstx2=ttk.Treeview(cariekr,height="60")
    
ttk.Style().theme_use("clam")    
ttk.Style().configure('Treeview',background='silver',foreground='green',fieldbackground="silver")
ttk.Style().map('Treeview',background=[('selected','green')])

veri3=pd.read_csv('oneh.csv',sep=',')
 #print(veri3)
vr3=pd.DataFrame(veri3)

vrx=vr3['v1']
a=[]
b=[]
vr3['mont']=vr3['v1'].str[0:2]
#print(vr3['mont'].replace('/',' '))
#(print(vr3['mont']))

for i in vr3['mont']:
    
    a.append(i.replace('/',' '))


for i in vr3['v1']:
    
    b.append(i.split('/'))
print(b)
input()
for i in range(0,len(b)):    
    b[i].pop(1)
    b[i]=b[i][0]+b[i][1]

vr3['mnt']=b
sonc=vr3.groupby('mnt').mean()
print(sonc)


print(sonc)

for i in vrx:
    
    vr3['v1']=dt.strptime(i,'%m/%d/%Y')

vrx=vr3['v1']






halt


        
    


   # trh=dt.strptime(i,'%d/%m/%Y')
   # print(trh)
#    print(vr3['Date'])
    





vr3['year'] = pd.DatetimeIndex(vr3['Date']).year
vr3['month_year'] = pd.to_datetime(vr3['Date']).dt.to_period('M')
#sonc=vr3.groupby('year').mean()
#sonc1=vr3.groupby('month_year').mean()

deg=' '

for i in range(1,72):
    deg= deg + ('v'+ str(i))+','


vr3['v1'] = pd.DatetimeIndex(vr3['v1']).year
vr3['month_year'] = pd.to_datetime(vr3['v1']).dt.to_period('M')
sonc=vr3.groupby('year').mean()
sonc1=vr3.groupby('month_year').mean()

   
print(sonc)



halt








vrx=vr3[['education','age', 'workclass','marital-status','occupation','relationship','sex','race','capital-gain']]


sonc=vrx.groupby('capital-gain').count()
print(sonc)
input()

   

#vr3=vr3.drop('status_type',axis=1)

#print(vr3['num_reactions'].mean())
#print(vr3['num_comments'].mean())
#print(vr3['num_shares'].mean())



input()
s=vr3.shape
print(s[0])



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
