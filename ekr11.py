from tkinter import *



pny=Tk()
pny.geometry("500x500")
frm=LabelFrame(pny,text="Listelenmek istenen değerler",width=350,height=260)
frm.place(x=10,y=220)
var=StringVar()
var1=StringVar()
var2=StringVar()
var3=StringVar()

ck=  Checkbutton(frm,text="Öğrenci No",variable=var,onvalue="ON",offvalue="OFF")


ck1=  Checkbutton(frm,text="Öğrenci adı",variable=var1,onvalue="ON",offvalue="OFF")
ck2=  Checkbutton(frm,text="Öğrenci soyadı",variable=var2,onvalue="ON",offvalue="OFF")
ck3=  Checkbutton(frm,text="Öğrenci Numarası",variable=var3,onvalue="ON",offvalue="OFF")
#ck1= Checkbutton(frm,text="Öğrenci Adı")
#ck2= Checkbutton(frm,text="ÖğrenciSoyadı")
#ck3= Checkbutton(frm,text="Öğrenci Not")
ck.deselect()
ck.place(x=30,y=80)
ck1.place(x=30,y=100)   #ck3.pack()
ck2.place(x=30,y=120)
ck3.place(x=30,y=140)

print(var.get())
