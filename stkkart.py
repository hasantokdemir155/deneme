from tkinter import *
from tkinter import ttk
import tkinter
import sqlite3


def stok():
    
    def tklal():
        stokkod=grss1.get()

        stokad=grss2.get()
        brim=grss3.get()
        alsfyat=int(grss4.get())
        satsfyat=int(grss5.get())
        adet=0
        
        kmt=bgln.cursor()  
        kmt.execute("insert into stokkart values(@p1,@p2,@p3,@p4,@p5,@p6)",(stokkod,stokad,brim,alsfyat,satsfyat,adet))  

        kmtl.execute("select stokkod,stokad,alsfyat,satsfyat from stokkart ")

        kaytlar=kmtl.fetchall()
        for rc1 in lstx22.get_children():
           lstx22.delete(rc1)

        for i in kaytlar:
           a= i[0]
           b=i[1]
           c=i[2]
           d=i[3]

           lstx22.insert('',"end",text="",values=(a,b,c,d))
 

        lstx22.pack(padx=5,pady=425)

        bgln.commit()
        bgln.close
    pn4=Tk()

    pn4.title("STOK KARTI")
    pn4.geometry("500x650")
    frm=Frame(pn4,width=350,height=25)
    frm.place(x=10,y=27)
    
    etkk=Label(pn4,text="STOK KODU",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=40)

    etkk1=Label(pn4,text="ÜRÜN ADI",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=92)

    etkk2=Label(pn4,text="ÜRÜN BİRİM",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=112)

    etkk3=Label(pn4,text="ALIŞ FİYAT",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=129)

    etkk4=Label(pn4,text="SATIŞ FİYAT",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=152)

    grss1=Entry(pn4,width=20)
    grss2=Entry(pn4)
    grss3=Entry(pn4)
    grss4=Entry(pn4)
    
    grss5=Entry(pn4)

    grss1.pack(padx=135,pady=37)
    grss2.pack(padx=185)
    grss3.pack(padx=185)
  

    grss4.pack(padx=185)
    grss5.pack(padx=185)


    btn14=Button(pn4,text="KAYDET",height=2,width=15,bg="GRAY",command=tklal).place(x=65,y=320)

    btn15=Button(pn4,text="KAPAT",height=2,width=15,bg="GRAY",command=pn4.destroy).place(x=185,y=320)

    lstx22=ttk.Treeview(frm,height="10")

    ttk.Style().theme_use("clam")    
    ttk.Style().configure('Treeview',background='silver',foreground='green',fieldbackground="silver")
    ttk.Style().map('Treeview',background=[('selected','green')])
        
    lstx22["columns"]= ("stokkod","stokad","satfyat","alfyat")

    lstx22.column("#0",width = 2)
    lstx22.column("stokkod",width=75)
    lstx22.column("stokad",width=60)
    lstx22.column("satfyat",width=80)
    lstx22.column("alfyat",width=95)  

    lstx22.heading("stokkod",text="stokkodu")    
    lstx22.heading("stokad",text="Ürün adı")
    lstx22.heading("satfyat",text="Satış fiyat")
                
    lstx22.heading("alfyat",text="Alış fiyat")
    bgln=sqlite3.connect("onmuhasebe.db")
    kmtl=bgln.cursor()
    kmtl.execute("select stokkod,stokad,satsfyat,alsfyat from stokkart ")
    kaytlar=kmtl.fetchall()
    for i in kaytlar:
          a= i[0]
          b=i[1]
          c=i[2]
          d=i[3]

          lstx22.insert('',"end",text="",values=(a,b,c,d))
 

    lstx22.pack(padx=5,pady=350)

    
    
