from tkinter import *
from tkinter import ttk
import tkinter
import sqlite3


def odemeaktar():
    a=grs11.get()
    b=grs13.get()
    c=grs14.get()
          #if grs != " " :      

    lstx2.insert('',"end",text="",values=(a,b,c))    
    lstx2.pack()    
    pass

def tahslataktar():
    d=grs11x.get()
    e=grs13x.get()
    f=grs14x.get()
          #if grs != " " :      

    lstx3.insert('',"end",text="",values=(d,e,f))    
    lstx3.pack()    
    pass
def kasanet():
     gg=[]     
     info=lstx2.get_children()
     gg1=[]     
     info1=lstx3.get_children()
     tplodm1=0
     tplodm=0
     for i in info:
         info2=lstx2.set(i)
          
         print([*info2.values()])
         gg=[*info2.values()]
         kod=gg[0]
         malkod=gg[1]
         odmmkt=int(gg[2])
         tplodm=tplodm+int(gg[2])

     for i in info1:
         info22=lstx3.set(i)
          
         print([*info22.values()])
         gg1=[*info22.values()]
         kod=gg1[0]
         malkod=gg1[1]
         
         tplodm1=tplodm1+int(gg1[2])
  
            
     print(tplodm1)  
     print(tplodm)       
     kln = tplodm-tplodm1
     sonc=Label(kspen,text="kASADAKİ miktar  "+str(kln)).place(x=165,y=425)
     
     pass


kspen=Tk()
kspen.geometry("900x500")

frm=Frame(kspen,width=200,height=75)
frm.place(x=10,y=50)

frm1=Frame(kspen,width=250,height=25)
frm1.place(x=160,y=100)

frm2=Frame(kspen,width=250,height=25)
frm2.place(x=490,y=50)


frm3=Frame(kspen,width=250,height=25)
frm3.place(x=420,y=100)


grs=Label(kspen,text="kasakod").place(x=35,y=25)
grsx=Label(kspen,text="ödemeyi yapan").place(x=165,y=25)
grsx=Label(kspen,text="ödeme miktarı").place(x=285,y=25)

Btnx=Button(kspen,text='Ödeme gir',command=odemeaktar).place(x=140,y=75)



grs11=Entry(frm)
grs11.grid(row=4,column=1)

grs13=Entry(frm)
grs13.grid(row=4,column=2)

grs14=Entry(frm)
grs14.grid(row=4,column=3)

grs1=Label(kspen,text="kasakod").place(x=490,y=20)
grsx1=Label(kspen,text="Tahsilatı alan").place(x=610,y=20)
grsx1=Label(kspen,text="Tahsilat miktarı").place(x=740,y=20)

Btnx1=Button(kspen,text='Tahsilat gir',command=tahslataktar).place(x=660,y=75)
Btnx2=Button(kspen,text='Kasanet hesapla',command=kasanet).place(x=390,y=45)



grs11x=Entry(frm2)
grs11x.grid(row=2,column=3)

grs13x=Entry(frm2)
grs13x.grid(row=2,column=4)

grs14x=Entry(frm2)
grs14x.grid(row=2,column=5)









lstx2=ttk.Treeview(frm1,height="14")

ttk.Style().theme_use("clam")    
ttk.Style().configure('Treeview',background='silver',foreground='green',fieldbackground="silver")
ttk.Style().map('Treeview',background=[('selected','green')])
        
lstx2["columns"]= ("Kaskod","odyap","odememkt")

lstx2.column("#0",width = 2)
lstx2.column("Kaskod",width=45)
lstx2.column("odyap",width=90)
lstx2.column("odememkt",width=110)       

lstx2.heading("Kaskod",text="Kasakodu")    
lstx2.heading("odyap",text="Ödeme Yapan")
lstx2.heading("odememkt",text="Ödeme miktarı")
                

lstx3=ttk.Treeview(frm3,height="14")

ttk.Style().theme_use("clam")    
ttk.Style().configure('Treeview',background='silver',foreground='green',fieldbackground="silver")
ttk.Style().map('Treeview',background=[('selected','green')])
        
lstx3["columns"]= ("Kaskod","tahslat","tahslatmkt")

lstx3.column("#0",width = 2)
lstx3.column("Kaskod",width=45)
lstx3.column("tahslat",width=90)
lstx3.column("tahslatmkt",width=110)       

lstx3.heading("Kaskod",text="Kasakodu")    
lstx3.heading("tahslat",text="Tahsilat Yapan")
lstx3.heading("tahslatmkt",text="Tahsilat miktarı")

