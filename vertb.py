import numpy as np
from sklearn import linear_model
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import cross_validate
from tkinter import *
from tkinter import ttk
import tkinter
import sqlite3
import matplotlib.pyplot as plt
import csv
import json
from ks import user
class veritbn():
    def __init__(self,k):
        self.bgln11=sqlite3.connect(k)
        self.kmt11=self.bgln11.cursor()
        self.kmt11.execute("select malad,sum(tutar) from islemsats group by(malad) ")
        self.kyt=self.kmt11.fetchall()
    def veral(self):
        with open('dnx.csv','w',newline='') as f:
            dosyekle=csv.writer(f,delimiter=',')

            for i in self.kyt:
                print(i[0]) 

                dosyekle.writerow(i)            

    def dtfram(self):
        self.veri3=pd.read_csv('dnx.csv',sep=',',header=None)
        self.vr=pd.DataFrame(self.veri3)
        print(self.vr)

json_us=json.loads(user)



with open('den2.json') as km:
    crs=json.load(km)
    for cr in crs:
        print(cr['owner']["html_url"])

hlt
k="onmuhasebe.db"
vrt=veritbn(k)
vrt.veral()
vrt.dtfram()

cariekr=Tk()

cariekr.geometry("500x500")



lstx2=ttk.Treeview(cariekr,height="60")
    
ttk.Style().theme_use("clam")    
ttk.Style().configure('Treeview',background='silver',foreground='green',fieldbackground="silver")
ttk.Style().map('Treeview',background=[('selected','green')])






lstx2["columns"]=("1","2")


lstx2.column('1',width=35)
lstx2.column('2',width=40)

lstx2.column("#0",width = 1)

       # lstx2.insert('',"end",text='',values=(i[0],i[1]))  
print('yyyyy')



print(vr)
lstx2.pack



