from tkinter import *
from tkinter import ttk

import sqlite3
def sonc():
     print(lkste.curselection())
     dst1=lkste.curselection()
     dst=lkste.get(dst1)
     
     kmt1.execute("select * from ogrnci,snflar where ogrnci.ogno=snflar.oggno and snflar.snf like '%"+ dst+"%' order by ogno")
     kaytlar=kmt1.fetchall()    

     lstx2=ttk.Treeview(frm1,height="14")
    
     lstx2["columns"]= ("ogrno","ogradı","ogrsoyad","ogrsnf")

     lstx2.column("#0",width = 2)

     lstx2.column("ogrno",width=40)
     lstx2.column("ogradı",width=40)
     lstx2.column("ogrsoyad",width=90)
     lstx2.column("ogrsnf",width=80)
        
        
     lstx2.heading("ogrno",text="Öğrencino")
     lstx2.heading("ogradı",text="Öğrenciadı")
     lstx2.heading("ogrsoyad",text="Öğrencisoyadı")
     lstx2.heading("ogrsnf",text="Öğrencisınıf")
    
     lstx2.tag_configure("ttk",background = "black")       

        
       
     for i in kaytlar:
    
           a=i[0]
           b=i[1]
           bb=i[2]
           dd=i[6]
        
  
           lstx2.insert('',"end",text="",values=(a,b,bb,dd))
  
     lstx2.pack(padx=20,pady=30)

     print(dst)     
     

pn3= Tk()
pn3.title("öğrenci liste ekranı")
pn3.geometry("500x500")

bgln1=sqlite3.connect("okul.db")
kmt1=bgln1.cursor()
frm=LabelFrame(pn3,text="Listelenmek istenen değerler",width=110,height=15)
frm.place(x=330,y=120)

kmt1.execute("select * from snflar group by  snf")

kaytlar=kmt1.fetchall()

lkste=Listbox(frm,width= 15,height=5)

for i in kaytlar:       
      
     lkste.insert(1,i[1])


#lkste.insert(END,"a")
lkste.pack(padx=10,pady=30)
frm1=LabelFrame(pn3,text="Sınıf Listesi",width=50,height=15)
frm1.place(x=20,y=5)

btn=Button(pn3,text="bas bakalım",command=sonc).place(x=220,y=390)




#btn=Button(pn3,text="bas bakalım",command=sonc)
#btn.pack


