from tkinter import *
from tkinter import ttk
import tkinter
import sqlite3

def dene():
    bgln11=sqlite3.connect("emlak.db")
    kmtll=bgln11.cursor()

    print('zzzzzzzz')       
    kmtll.execute("select evkod,alckod,evdrum,kmsyon,satcad,satsfyat from satlanlar")
    kaytlar=kmtll.fetchall()

#mytab=ttk.Notebook(pn5)
#mytab.pack(pady=5)
#mytab1= ttk.Frame(mytab,width=700,height=500)
#mytab.add(mytab1,text="SATILANLAR Listesi")

 #pn8.destroy()
    pn5=tkinter.Tk()

    lstx2=ttk.Treeview(pn5,height="14")

    ttk.Style().theme_use("clam")
    ttk.Style().configure('Treeview',background='silver',foreground='green',fieldbackground="silver")
    ttk.Style().map('Treeview',background=[('selected','purple')])

    lstx2["columns"]= ("Evkod","Alckod","Talpdrm")
    lstx2.column("#0",width = 2)
    lstx2.column("Evkod",width=60)
    lstx2.column("Alckod",width=60)
    lstx2.column("Talpdrm",width=80)
 
    lstx2.heading("Evkod",text="Ev Kodu")
    lstx2.heading("Alckod",text="Alıcıkodu")
    lstx2.heading("Talpdrm",text="Evin durumu")


#kaytlar=[('e','s','d'),('c','f','d'),('k','f','l')]

    for i in kaytlar:
    
            a=i[0]
            b=i[1]
            bb=str(i[2])
          
            
            lstx2.insert('',"end",text="",values=(a,b,bb))
 
    lstx2.pack(padx=20,pady=30)        
    



def oyn():    
    bgln11=sqlite3.connect("emlak.db")
    kmtll=bgln11.cursor()


    pn8=tkinter.Tk()
    Btnx=Button(pn8,text='basssss',command=dene)
    Btnx.pack()

