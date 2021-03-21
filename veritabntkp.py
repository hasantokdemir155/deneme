from tkinter import *
from tkinter import ttk
import tkinter
import sqlite3







def adsra():

    for rc1 in lstx31.get_children():
          lstx31.delete(rc1)
          
    kmtl.execute("select  no,ad,soyad,bolum,adress,rkam,telefon from tab1 order by ad")  
    kaytlar=kmtl.fetchall()
 
    
    for i in kaytlar:
         a=i[0]
         bb=i[4] 
         b=i[1]
         c=i[2]
         d=i[3]
         e=i[5]
         f=i[6]
             
          
         lstx31.insert('',"end",text="",values=(a,b,c,d,bb,e,f))




    lstx31.pack()

def soyadsra():
    for rc1 in lstx31.get_children():
          lstx31.delete(rc1)
          
    kmtl.execute("select  no,ad,soyad,bolum,adress,rkam,telefon from tab1 order by soyad")  
    kaytlar=kmtl.fetchall()
 
    
    for i in kaytlar:
         a=i[0]
         bb=i[4] 
         b=i[1]
         c=i[2]
         d=i[3]
         e=i[5]
         f=i[6]
             
          
         lstx31.insert('',"end",text="",values=(a,b,c,d,bb,e,f))




    lstx31.pack()
    

def bolumsra():
    for rc1 in lstx31.get_children():
          lstx31.delete(rc1)
          
    kmtl.execute("select  no,ad,soyad,bolum,adress,rkam,telefon from tab1 order by bolum")  
    kaytlar=kmtl.fetchall()
 
    
    for i in kaytlar:
         a=i[0]
         bb=i[4] 
         b=i[1]
         c=i[2]
         d=i[3]
         e=i[5]
         f=i[6]
             
          
         lstx31.insert('',"end",text="",values=(a,b,c,d,bb,e,f))




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

#kmtl.execute("select  no,ad,soyad,bolum,adress,rkam,telefon from tab1")  
#kaytlar=kmtl.fetchall()

#for i in kaytlar:
#     a=i[0]
#     bb=i[4] 
#     b=i[1]
#     c=i[2]
#     d=i[3]
#     e=i[5]
#     f=i[6]
     #print(a,b,c,d)    
          
#     lstx31.insert('',"end",text="",values=(a,b,c,d,bb,e,f))




lstx31.pack()

Btnx=Button(genkekr,text='ada göre sıra',command=adsra).place(x=112,y=1)
Btnx1=Button(genkekr,text='soyaada göre sıra',command=soyadsra).place(x=193,y=1)
Btnx2=Button(genkekr,text='bölüme göre sıra',command=bolumsra).place(x=298,y=1)

