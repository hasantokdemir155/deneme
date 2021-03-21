from tkinter import *
import sqlite3

def tkla():
   
    ogno=int(grs.get())
    ogad=grs1.get()
    osoyad=grs2.get()
    ogfyat=int(grs3.get())
    ognot=int(grs4.get())

    kmt.execute("insert into ogrnci values(@p1,@p2,@p3,@p4,@p5)",(ogno,ogad,osoyad,ogfyat,ognot))  
    bgln.commit()
    bgln.close
 
   

#def vertaban() :
    
 #   kmt.execute("create table if not exists ogrnci(ogno integer,ogad text,osoyad text,ogfyat integer,ognot integer)")
 #   bgln.commit()

#def bglnvertb():

bgln=sqlite3.connect("okul.db")
kmt=bgln.cursor()
    
#bglnvertb()

pn1= Tk()
pn1.title("öğrenci kayıt ekranı")
pn1.geometry("400x400")
grs=Entry(pn1)

btn1=Button(pn1,text="KAYDET",width=20,bg="green",command=tkla).place(x=70,y=270)
btn2=Button(pn1,text="ÇIKIŞ",width=20,bg="blue",command=pn1.destroy).place(x=220,y=270)

#btn1.pack(side="top")




etk=Label(pn1,text="ÖĞRENCİ NO",font=("Bold",10)
          #width= 20,
).place(x=25,y=35)

etk1=Label(pn1,text="ÖĞRENCİ ADI",font=("Bold",10)
          #width= 20,
).place(x=25,y=85)

etk2=Label(pn1,text="ÖĞRENCİ SOYADI",font=("Bold",10)
          #width= 20,
).place(x=25,y=105)

etk3=Label(pn1,text="ÖĞRENCİ ÜCRETİ",font=("Bold",10)
          #width= 20,
).place(x=25,y=125)
etk4=Label(pn1,text="ÖĞRENCİ NOTU",font=("Bold",10)
          #width= 20,
).place(x=25,y=145)
    

grs.grid(row=2,column=1)

grs.pack(padx=140,pady=35,anchor=NW)
grs1=Entry(pn1)
grs2=Entry(pn1)
grs3=Entry(pn1)
grs4=Entry(pn1)

grs1.pack()
grs2.pack()
grs3.pack()
grs4.pack()


pn1.mainloop()
