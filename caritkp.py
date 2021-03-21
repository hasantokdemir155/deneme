from tkinter import *
import sqlite3
from tkinter import ttk


def gencar():
     #lstx2.destroy()     
     kmtl=bglnl.cursor()
     kmtl.execute("drop view dnmlx")
     kmtl.execute("CREATE VIEW dnmlx  as select sum (tutar)  ttr,msterkod,odenen,iskod from islemsats group by iskod")
     #kmtl.execute("select  msterkod,odenen from islemsats group by iskod")
     kayt=kmtl.fetchall()
     print(kayt)
     kmtl.execute("select sum(ttr),sum(odenen), msterkod from dnmlx group by msterkod")
     kaytlar=kmtl.fetchall()

     for rc1 in lstx3.get_children():
          lstx3.delete(rc1)
     for rc in lstx2.get_children():
          lstx2.delete(rc)
     tbrc=0
     odmktr=0
     tpkln=0
     for i in kaytlar:
          kln= i[0]-i[1]
          tt=i[0]
          od=i[1]
          mst=i[2]

          tpkln= tpkln + int(kln)
          tbrc = tbrc + int(i[0])
          odmktr = odmktr + int(i[1])
          
          #print(i)
          lstx3.insert('',"end",text="",values=(mst,tt,od,kln))
     etk2=Label(cariekr,text="Genel borc",font=("Bold",12)
          #width= 20,
     ).place(x=320,y=465)
     etk21=Label(cariekr,text="Ödenen borc"+" "+ str(odmktr),font=("Bold",12)
          #width= 20,
     ).place(x=515,y=465)
     etk22=Label(cariekr,text=str(tbrc)+" TL",font=("Bold",12)
          #width= 20,
     ).place(x=420,y=465)     
     lstx3.pack(padx=65,pady=114)
     etk23=Label(cariekr,text="Toplam Kalan"+" "+ str(tpkln),font=("Bold",12)
          #width= 20,
     ).place(x=640,y=465)
     
def cardok():
     #lstx3.destroy()
     bb=mcmb3.get()   
     kmtl=bglnl.cursor()
     kmtl.execute("create view dnms as select sum(tutar) tut,msterkod,odenen,iskod from islemsats where  msterkod like '%" + mcmb3.get()+"%' group by iskod")  
     kaytlar=kmtl.fetchall()
         
     for rc1 in lstx3.get_children():
          lstx3.delete(rc1)

     for rc in lstx2.get_children():
          lstx2.delete(rc)
     ttr=0
     odn=0
     for i in kaytlar:
         #print(i) 
         a=i[1]
         b=i[0]
         c=i[2]
         d=i[3]
         ttr=ttr+ int(b)
         odn=odn+int(c)
      
          
         lstx2.insert('',"end",text="",values=(a,b,c,d))
     print(ttr,odn)     
     borc=ttr-odn
     etk1=Label(cariekr,text="Müşteri borcu",font=("Bold",14)
          #width= 20,
     ).place(x=78,y=465)
     etk=Label(cariekr,text=str(borc)+" TL",font=("Bold",14)
          #width= 20,
     ).place(x=195,y=465)
     #print(ttr,odn)
     lstx2.pack(padx=5,pady=125)



cariekr=Tk()
cariekr.geometry("800x500")

frm=Frame(cariekr,width=750,height=25)
frm.place(x=10,y=30)

frm1=Frame(cariekr,width=750,height=25)
frm1.place(x=350,y=37)


bglnl=sqlite3.connect("onmuhasebe.db")
kmtl=bglnl.cursor()
#kmt1.execute("select musterad from msteri group by musterad")
kmtl.execute("select msterkod from islemsats group by msterkod")
kaytlar=kmtl.fetchall()
#print(kaytlar)
lstcmb=[]

for i in kaytlar:
  print(i[0])   
  lstcmb.append(i[0])
print(lstcmb)

mcmb3=ttk.Combobox(cariekr,values=lstcmb,width=16)
mcmb3.place(x=76,y=27)

#mcmb3['values'].append(kaytlar)
#print(mcmb3['values'])
mcmb3.current(0)


Btnx=Button(cariekr,text='CARİ DÖKÜM',command=cardok,borderwidth=15).place(x=420,y=27)
Btnx1=Button(cariekr,text='genelCARİ DÖKÜM',command=gencar,borderwidth=15).place(x=560,y=27)


lstx2=ttk.Treeview(frm,height="14")

ttk.Style().theme_use("clam")    
ttk.Style().configure('Treeview',background='silver',foreground='green',fieldbackground="silver")
ttk.Style().map('Treeview',background=[('selected','green')])
        
lstx2["columns"]= ("musad","altutar","odenen","islemkod")

lstx2.column("#0",width = 2)
lstx2.column("musad",width=75)
lstx2.column("altutar",width=60)
lstx2.column("odenen",width=80)
lstx2.column("islemkod",width=95)  
        
        

lstx2.heading("musad",text="müşteri")    
lstx2.heading("altutar",text="tutar")
lstx2.heading("odenen",text="ödenen")
                
lstx2.heading("islemkod",text="işlemkodu")



lstx3=ttk.Treeview(frm1,height="14")

ttk.Style().theme_use("clam")    
ttk.Style().configure('Treeview',background='silver',foreground='green',fieldbackground="silver")
ttk.Style().map('Treeview',background=[('selected','green')])
        
lstx3["columns"]= ("musad","altutar","odenen","kalan")

lstx3.column("#0",width = 2)
lstx3.column("musad",width=75)
lstx3.column("altutar",width=60)
lstx3.column("odenen",width=80)
lstx3.column("kalan",width=95)  
        
        

lstx3.heading("musad",text="müşteri")    
lstx3.heading("altutar",text="tutar")
lstx3.heading("odenen",text="ödenen")
                
lstx3.heading("kalan",text="kalan borç")




