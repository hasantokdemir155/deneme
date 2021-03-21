from tkinter import *
from tkinter import ttk
import pandas as pd
import csv
from datetime import datetime as dt

import time


class veriok():
    
    def __init__(self,m):
        self.veri=pd.read_csv(m,',',header=None)

        print(self.veri)
    def grpla(self):
        self.vr=pd.DataFrame(self.veri)
        print(self.vr.groupby(0).count())
    def kolek(self):    
        self.vr['ekkol']=self.vr[23]-1
        print(self.vr)


#veri=pd.read_csv('ogrnci.csv')
#vr=pd.DataFrame(veri,columns=['ogad','ogsoyad','ogfyat'])
                               
#print(vr)
#ogsoyad,ogfyat
        
m='allbp.csv'
pnds=veriok(m)

    

pnds.grpla()
pnds.kolek()
