from tkinter import *
from tkinter import ttk
import tkinter
import sqlite3
import random




x1=random.randint(3,10)
print(x1)

bglnl=sqlite3.connect("denme.db")

kmt1=bglnl.cursor()
#kmt1.execute("select stokad,stokkod from stokkart group by stokad")
#kaytlar=kmt1.fetchall()

#kmt1=bglnl.cursor()
#kmt1.execute("select musterad from msteri group by musterad")
#kaytlar2=kmt1.fetchall()

#print(kaytlar[0][0])
#print(kaytlar2[1][0])

#bglnl.commit()
#bglnl.close
#bglnl=sqlite3.connect("onmuhasebe.db")
#kmt1=bglnl.cursor()
#print(kaytlar2)

#print(type(kaytlar2))
#  (tab1 = no,ad,soyad,bolum,adress,rkam,telefon)

adlar=['ali','cem','hakan','salih','selim','aytek','belgin']
soyadlar=['keremci','gül','sem','fonek','toprak','şemaver','feli']
adresler= ['hnhnhg thnh','dnnmbnm','utyuıuyu','oyuotı','uıyunmbnbm','qwerttrty yyt','zxvncvbbvb']

bolumler=['tyt','ghgj','tyuu','rtyu']

for i in range(1,100):
        

    x1=random.randint(0,6)
    s1=random.randint(0,6)
    z1=random.randint(0,6)
    m1= random.randint(0,3)
    ad = adlar[x1]
    soyad = soyadlar[s1]
    adress= adresler[z1]
    rkam=int(random.randint(60,145))
    telefon = int(random.randint(24568,37345))
    no = random.randint(1,100)
    bolum=bolumler[m1]
   


    print(no,ad,soyad,bolum,adress,rkam,telefon)
    kmt1.execute("insert into tab1 values(@p1,@p2,@p3,@p4,@p5,@p6,@p7)",
                    
    (no,ad,soyad,bolum,adress,rkam,telefon))
      
        
bglnl.commit()
bglnl.close

    
