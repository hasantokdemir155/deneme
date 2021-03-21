from tkinter import *
from tkinter import ttk
import tkinter
import sqlite3
import pandas as pd

def veri():
    bx=mcmb4.get()   
    
    for rc in lstx31.get_children():
          lstx31.delete(rc)
    for rc1 in lstx31.get_children():
          lstx31.delete(rc1)
         
    kmtl=bglnl.cursor()
    kmtl.execute("select no,ad,soyad,bolum,adress,rkam,telefon from tab1 where  bolum like '%" + mcmb4.get()+"%'")
    kmtx=bglnl.cursor()
    kmtx.execute("select sum(rkam) from tab1 where  bolum like '%" + mcmb4.get()+"%'")  

    kaytlar=kmtl.fetchall()

    kaytlars=kmtx.fetchall()

    
    
    for i in kaytlars:
        
        mc=i[0]
        
   
    for i in kaytlar:
         a=i[0]
         bb=i[4] 
         b=i[1]
         c=i[2]
         d=i[3]
         e=i[5]
         f=i[6]
         
          
         lstx31.insert('',"end",text="",values=(a,b,c,d,bb,e,f))
    etk1=Label(genkekr,text="Total rakam",font=("Bold",14)
          #width= 20,
     ).place(x=365,y=465)
    etk=Label(genkekr,text=str(mc),font=("Bold",14)
          #width= 20,
     ).place(x=485,y=465)

    
    lstx31.pack()




    






bglnl=sqlite3.connect("denme.db")

kmtl=bglnl.cursor()

genkekr=Tk()
genkekr.geometry("800x500")
#frm=Frame(genkekr,width=250,height=25)
#frm.place(x=5,y=30)

frm1=Frame(genkekr,width=650,height=25)
frm1.place(x=65,y=26)

lstx31=ttk.Treeview(frm1,height="19")

ttk.Style().theme_use("clam")    
ttk.Style().configure('Treeview',background='silver',foreground='green',fieldbackground="silver")
ttk.Style().map('Treeview',background=[('selected','green')])
        #(tab1 = no,ad,soyad,bolum,adress,rkam,telefon)
lstx31["columns"]= ("no","ad","soyad","bolum","adres","rkam","telefon")

lstx31.column("#0",width = 2)
lstx31.column("no",width=29)
lstx31.column("ad",width=76)
lstx31.column("soyad",width=88)
lstx31.column("bolum",width=85)
lstx31.column("adres",width=88)
lstx31.column("rkam",width=58)

lstx31.column("telefon",width=78)

        
        

lstx31.heading("no",text="no")    
lstx31.heading("ad",text="ADI")
lstx31.heading("soyad",text="SOYAD")
lstx31.heading("bolum",text="BÖLÜMÜ")
lstx31.heading("adres",text="ADRESİ")

lstx31.heading("rkam",text="RAKAM")
lstx31.heading("telefon",text="TELEFON")

kmtl.execute("select  no,ad,soyad,bolum,adress,rkam,telefon from tab1")  
kaytlar=kmtl.fetchall()

for i in kaytlar:
     a=i[0]
     bb=i[4] 
     b=i[1]
     c=i[2]
     d=i[3]
     e=i[5]
     f=i[6]
     #print(a,b,c,d)    
          
     lstx31.insert('',"end",text="",values=(a,b,c,d,bb,e,f))

df=pd.DataFrame(kaytlar)
dfx=df.groupby(3).sum()
print(dfx[5])

lstx31.pack()
#(tab1 = no,ad,soyad,bolum,adress,rkam,telefon)

kmt1=bglnl.cursor()
kmt1.execute("select bolum from tab1 group by bolum")
kaytlar=kmt1.fetchall()


    
mcmb4=ttk.Combobox(genkekr,width=16)
mcmb4.place(x=276,y=1)
mcmb4['values']=kaytlar
print(mcmb4['values'])
mcmb4.current(0)    








Btnx=Button(genkekr,text='verileri getir',command=veri).place(x=441,y=1)
