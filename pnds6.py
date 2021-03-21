from tkinter import *
from tkinter import ttk
import pandas as pd
import csv


cariekr=Tk()
cariekr.geometry("900x900")

lstx2=ttk.Treeview(cariekr,height="60")
    
ttk.Style().theme_use("clam")    
ttk.Style().configure('Treeview',background='silver',foreground='green',fieldbackground="silver")
ttk.Style().map('Treeview',background=[('selected','green')])

veri3=pd.read_csv('adult.csv',sep=', ')
 #print(veri3)
vr3=pd.DataFrame(veri3)
print(vr3)
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
