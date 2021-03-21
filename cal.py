import numpy as np
from sklearn import datasets,svm
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
import pandas as pd
from tkinter import *
from tkinter import ttk


def veral():
    
    veri2=datasets.load_linnerud()    
    vr2=pd.DataFrame(veri2.data,columns=['Chins', 'Situps', 'Jumps'])
    print(veri2.feature_names)
    lstx2=ttk.Treeview(cariekr,height="21")
    
    ttk.Style().theme_use("clam")    
    ttk.Style().configure('Treeview',background='silver',foreground='green',fieldbackground="silver")
    ttk.Style().map('Treeview',background=[('selected','green')])
    lstx2["columns"]= (veri2.feature_names)
    print(lstx2["columns"])
    lstx2.column("#0",width = 2)
    print(vr2.loc[:])

    print(vr2['Chins'].mean())

    for i in lstx2["columns"]:
        lstx2.column(i,width=85)
        

    for i in lstx2["columns"]:
        lstx2.heading(i,text=i) 
    print(vr2.iloc[0,0])
    sm=vr2.shape
    print(sm[0],sm[1])

    for k in range(0,sm[0]):
        for l in range(0,sm[1]):
            a=vr2.iloc[k,l]
            b=vr2.iloc[k,l+1]
            c=vr2.iloc[k,l+2]
            break
           
        
        lstx2.insert('',"end",text="",values=(a,b,c))
    lstx2.pack()
    
veri=datasets.load_diabetes()
vr=pd.DataFrame(veri.data,columns=['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6'])

#print(veri.feature_names)

#print(vr)


cariekr=Tk()
cariekr.geometry("500x500")



Btnx=Button(cariekr,text='verial',command=veral,borderwidth=15).place(x=120,y=27)
