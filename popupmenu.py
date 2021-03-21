from tkinter import *


def stokkart():
    pass


cls=Tk()
cls.geometry("400x400")


mxmenu=Menu(cls)
cls.config(menu=mxmenu)


kayt=Menu(mxmenu)
fatra=Menu(mxmenu)
rapor=Menu(mxmenu)

mxmenu.add_cascade(label="Kayıt Kartı",menu=kayt)
kayt.add_command(label="Stok kartı",command=stokkart)

kayt.add_command(label="Müşteri kartı",command=stokkart)

kayt.add_command(label="Tedarikçi kartı",command=stokkart)
#kayt.insert_separator(1)
kayt.insert_separator(2)
kayt.insert_separator(4)



#mxmenu.add_separator()

mxmenu.add_cascade(label="Fatura Giriş",menu=fatra)
fatra.add_command(label="Satış Fatura Giriş")
fatra.add_command(label="Alış Fatura Giriş")

mxmenu.add_cascade(label="Raporlar",menu=rapor)
rapor.add_command(label="Cari Döküm Müşteri")
rapor.add_command(label="Cari Döküm Tedarikçi")
rapor.add_command(label="Stok Döküm Ürün Bazlı")
rapor.add_command(label="Mevcut stok genel")
rapor.add_command(label="Mevcut Kasa Durumu")



cls.mainloop()
