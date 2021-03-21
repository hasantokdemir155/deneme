from tkinter import *
from tkinter import ttk
import pandas as pd



cariekr=Tk()
cariekr.geometry("500x500")

lstx2=ttk.Treeview(cariekr,height="21")
    
ttk.Style().theme_use("clam")    
ttk.Style().configure('Treeview',background='silver',foreground='green',fieldbackground="silver")
ttk.Style().map('Treeview',background=[('selected','green')])


veri3=pd.read_csv('adult.csv',sep=', ')
#print(veri3)
vr3=pd.DataFrame(veri3)
cm=[]
#print(vr3)
#print()
vrx=vr3[["age","workclass","fnlwgt"]]

vm=vrx[10:45]
vm1=vm['age']
vm11=vm['workclass']
vm22=vm['fnlwgt']


s=vm1[3:25]
s11=vm11[3:25]
s22=vm22[3:25]



lstx2["columns"]= ("v1","v2","v3")


lstx2.column("v1",width=40)
lstx2.column("v2",width=70)
lstx2.column("v3",width=95)


print(s)
#print(vm1[10:13])

#lstx2["columns"]= cm
#print(lstx2["columns"])
lstx2.column("#0",width = 2)

a=[]
print(type(s))
k=s.to_list()
k1=s11.to_list()
k2=s22.to_list()

for i in range(0,21,1):
    a.append(k[i])
    a.append(k1[i])
    a.append(k2[i])
    print(k[i])
    lstx2.insert('',"end",text='',values=(a))
    a=[]
     
lstx2.pack()



   # if s > 3:
     #    break
