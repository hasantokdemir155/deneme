from tkinter import *
from tkinter import ttk
import sqlite3

class ekran:
    #global mcmb
    def __init__(self,m,n,s,g):        
        self.m=m
        self.n=n
        self.s=s
        self.g=g
        #self.mcmb=mcmb
       
    def kmb(self):
        
        self.mcmb=ttk.Combobox(self.s)
        self.mcmb.place(x=self.m,y=self.n)
        self.mcmb['values']=self.g
         
    def combtk(self): 
        self.sk=self.mcmb.get()
        self.bglnl=sqlite3.connect("emlak.db")

        self.kmt1=bgln1.cursor()

        self.kmt1.execute("select alckodu,talepstat,istenensemt from alc where alckodu like '%"+ self.sk+"%' ") 
        self.kaytlar=self.kmt1.fetchall()   
        
        #etkx=Label(pnx,text = mcmb.get())

        self.pnx1=Tk()

        self.pnx1.geometry('350x350')    
        self.lstx1=ttk.Treeview(self.pnx1,height="14")

        self.lstx1["columns"]= z

        self.lstx1.column("#0",width = 2)

        self.lstx1.column("Alckod",width=70)
        self.lstx1.column("Talpstat",width=90)
        self.lstx1.column("istsemt",width=90)
              
        
        self.lstx1.heading("Alckod",text="Alıcıkodu")
        self.lstx1.heading("Talpstat",text="Evin durumu")
        self.lstx1.heading("istsemt",text="Semti")
        
        
    
        for i in self.kaytlar:
    
            a=i[0]
            b=i[1]
            c=i[2]
           
            
            self.lstx1.insert('',"end",text="",values=(a,b,c))
      

        print(self.kaytlar)
        self.lstx1.pack(padx=20,pady=30) 
    
pnx=Tk()

pnx.geometry('350x350')

etkk=Label(pnx,text="ALICIKODU",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=36)

a='satılık'
b='kiralık'

bgln1=sqlite3.connect("emlak.db")
kmt1=bgln1.cursor()
kmt1.execute("select alckodu from alc order by alckodu") 
kaytlar=kmt1.fetchall()   
g=kaytlar
cmbx=ekran(65,190,pnx,g)
z="Alckod","Talpstat","istsemt"
grs1=Entry(pnx,width=35)
grs1.pack(padx=115,pady=35)


btn=Button(pnx,text='tıkla canım',command=cmbx.combtk).place(x=85,y=170)


cmbx.kmb()

