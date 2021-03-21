from tkinter import *
from tkinter import ttk
import tkinter
import sqlite3



def mstri():
    
    def tkla():
        musterkod=grss1.get()

        musterad=grss2.get()
        musteradres=grss3.get()
        musteril=grss4.get()
        musterborc=int(grss5.get())

        bgln=sqlite3.connect("onmuhasebe.db")

        kmt=bgln.cursor()  
        kmt.execute("insert into msteri values(@p1,@p2,@p3,@p4,@p5)",(musterkod,musterad,musteradres,musteril,musterborc))  

        bgln.commit()
        bgln.close

    pn4=Tk()

    pn4.title("MÜŞTERİ KARTI")
    pn4.geometry("500x550")

    etkk=Label(pn4,text="MÜŞTERİ KODU",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=40)

    etkk1=Label(pn4,text="MÜŞTERİ ADI",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=92)

    etkk2=Label(pn4,text="MÜŞTERİ ADRES",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=112)

    etkk3=Label(pn4,text="MÜŞTERİ İL",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=129)

    etkk4=Label(pn4,text="BORÇ",font=("Bold",10)
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

    

    btn14=Button(pn4,text="KAYDET",height=2,width=15,bg="GRAY",command=tkla).place(x=65,y=320)

    btn15=Button(pn4,text="KAPAT",height=2,width=15,bg="GRAY",command=pn4.destroy).place(x=185,y=320)



    
    
