from tkinter import *
from tkinter import ttk
import tkinter
import sqlite3

class ekran:
    def __init__(self):
        
        self.frm=Frame(kspen,width=200,height=75)
        self.frm.place(x=10,y=50)

        self.frm1=Frame(kspen,width=250,height=25)
        self.frm1.place(x=160,y=100)

        self.frm2=Frame(kspen,width=250,height=25)
        self.frm2.place(x=490,y=50)

        self.frm3=Frame(kspen,width=250,height=25)
        self.frm3.place(x=420,y=100)
        
        self.lstx2=ttk.Treeview(self.frm1,height="14")
        self.lstx2["columns"]= ("Kaskod","odyap","odememkt")

        self.lstx2.column("#0",width = 2)
        self.lstx2.column("Kaskod",width=45)
        self.lstx2.column("odyap",width=90)
        self.lstx2.column("odememkt",width=110)       

        self.lstx2.heading("Kaskod",text="Kasakodu")    
        self.lstx2.heading("odyap",text="Ödeme Yapan")
        self.lstx2.heading("odememkt",text="Ödeme miktarı")
                

        self.lstx3=ttk.Treeview(self.frm3,height="14")

        
        self.lstx3["columns"]= ("Kaskod","tahslat","tahslatmkt")

        self.lstx3.column("#0",width = 2)
        self.lstx3.column("Kaskod",width=45)
        self.lstx3.column("tahslat",width=90)
        self.lstx3.column("tahslatmkt",width=110)       

        self.lstx3.heading("Kaskod",text="Kasakodu")    
        self.lstx3.heading("tahslat",text="Tahsilat Yapan")
        self.lstx3.heading("tahslatmkt",text="Tahsilat miktarı")
        
    def grsler(self):
        self.grs=Label(kspen,text="kasakod").place(x=35,y=25)
        self.grsx=Label(kspen,text="ödemeyi yapan").place(x=165,y=25)
        self.grsx=Label(kspen,text="ödeme miktarı").place(x=285,y=25)





        self.grs11=Entry(self.frm)
        self.grs11.grid(row=4,column=1)

        self.grs13=Entry(self.frm)
        self.grs13.grid(row=4,column=2)

        self.grs14=Entry(self.frm)
        self.grs14.grid(row=4,column=3)

        self.grs1=Label(kspen,text="kasakod").place(x=490,y=20)
        self.grsx1=Label(kspen,text="Tahsilatı alan").place(x=610,y=20)
        self.grsx1=Label(kspen,text="Tahsilat miktarı").place(x=740,y=20)


        self.grs11x=Entry(self.frm2)
        self.grs11x.grid(row=2,column=3)

        self.grs13x=Entry(self.frm2)
        self.grs13x.grid(row=2,column=4)

        self.grs14x=Entry(self.frm2)
        self.grs14x.grid(row=2,column=5)
          
    def lsteler():
        
        pass    
        
    
    
    def odemeaktar(self):
        self.a=self.grs11.get()
        self.b=self.grs13.get()
        self.c=self.grs14.get()
        print(self.a)
          #if grs != " " :      

        self.lstx2.insert('',"end",text="",values=(self.a,self.b,self.c))    

        self.lstx2.pack()    
        pass

    def tahslataktar(self):
        self.d=self.grs11x.get()
        self.e=self.grs13x.get()
        self.f=self.grs14x.get()
          #if grs != " " :      

        self.lstx3.insert('',"end",text="",values=(self.d,self.e,self.f))    
        self.lstx3.pack()    
        pass

kspen=Tk()
kspen.geometry("900x500")

kasaekran=ekran()
kasaekran.grsler()




Btnx=Button(kspen,text='Ödeme gir',command=kasaekran.odemeaktar).place(x=140,y=75)
Btnx1=Button(kspen,text='Tahsilat gir',command=kasaekran.tahslataktar).place(x=660,y=75)









ttk.Style().theme_use("clam")    
ttk.Style().configure('Treeview',background='silver',foreground='green',fieldbackground="silver")
ttk.Style().map('Treeview',background=[('selected','green')])


