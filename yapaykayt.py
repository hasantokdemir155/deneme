from tkinter import *
from tkinter import ttk
import tkinter
import sqlite3
import random




x1=random.randint(3,10)
print(x1)

bglnl=sqlite3.connect("onmuhasebe.db")
kmt1=bglnl.cursor()
kmt1.execute("select stokad,stokkod from stokkart group by stokad")
kaytlar=kmt1.fetchall()

kmt1=bglnl.cursor()
kmt1.execute("select musterad from msteri group by musterad")
kaytlar2=kmt1.fetchall()

#print(kaytlar[0][0])
#print(kaytlar2[1][0])
bglnl.commit()
bglnl.close
bglnl=sqlite3.connect("onmuhasebe.db")
kmt1=bglnl.cursor()
#print(kaytlar2)

#print(type(kaytlar2))

for i in range(1,100000):
    x1=random.randint(3,10)
    odenen=int(random.randint(60,145))
    iskod="is"+str(i)
    print("yeni fatura",str(x1),i)
    s1=random.randint(0,6)
    for k in range(1,x1):
        
        y1=random.randint(1,6)
        mk1=random.randint(10,25)
        sf=random.randint(1,15)

        malkod=kaytlar[y1][1]
        malad=kaytlar[y1][0]
        mktar=int(mk1)
        satfyat=int(sf)
        msterkod=kaytlar2[s1][0]
        
        tutar=sf*mk1
        #print(iskod,malkod,malad,mktar,satfyat,msterkod,tutar,odenen)
        kmt1.execute("insert into islemsats values(@p1,@p2,@p3,@p4,@p5,@p6,@p7,@p8)",
                    
                      (iskod,malkod,malad,mktar,satfyat,msterkod,odenen,tutar))
      
        
bglnl.commit()
bglnl.close

    
