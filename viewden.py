from tkinter import *
import sqlite3
from tkinter import ttk

bglnl=sqlite3.connect("onmuhasebe.db")
kmtl=bglnl.cursor()
kmt2=bglnl.cursor()
#kmtl.execute("drop view dnmlx1")
     #kmtl.execute("CREATE VIEW dnmlx  as select sum (tutar)  ttr,msterkod,odenen,iskod from islemsats group by iskod")
#kmtl.execute("select  amalad,sum(amaladet),sum(mktar),amalkod from islemals,islemsats where islemals.amalkod=islemsats.malkod")
kmt2.execute("select  amalad,sum(amaladet),amalkod,amalfyat from islemals group by amalkod")
kmtl.execute("select  malad,sum(mktar),malkod from islemsats group by malkod")

kaytlar=kmtl.fetchall()
kaytlar1=kmt2.fetchall()

stokekr=Tk()
stokekr.geometry("800x500")

lstx3=ttk.Treeview(stokekr,height="14")

ttk.Style().theme_use("clam")    
ttk.Style().configure('Treeview',background='silver',foreground='green',fieldbackground="silver")
ttk.Style().map('Treeview',background=[('selected','green')])
        
lstx3["columns"]= ("stokad","satlan","alnan","kalan","fyat","stoktutar")

lstx3.column("#0",width = 2)
lstx3.column("stokad",width=75)
lstx3.column("satlan",width=76)
lstx3.column("alnan",width=88)
lstx3.column("kalan",width=88)
lstx3.column("fyat",width=88)

lstx3.column("stoktutar",width=88)

        
        

lstx3.heading("stokad",text="stokadı")    
lstx3.heading("satlan",text="alınan adet")
lstx3.heading("alnan",text="satılan adet")
lstx3.heading("kalan",text="kalan adet")
lstx3.heading("fyat",text="alım fiyatı")

lstx3.heading("stoktutar",text="stok tutarı")

gtplm=0
for i in kaytlar:
    for t in kaytlar1:
        if i[0] == t[0]:
            print(i[0],t[1],i[1])
            a=i[0]
            b=int(t[1])
            c=int(i[1])
            d=b-c
            e=int(t[3])
            tplfyt=int(d)*int(t[3])
            gtplm= gtplm + tplfyt
            lstx3.insert('',"end",text="",values=(a,b,c,d,e,tplfyt))
            break
    if i[0]!= t[0]:        
        #print(i[0],t[0])
        a=i[0]
        b="0"
        c=int(i[1])
        d=c
        e=int(t[3])
        tplfyt=int(d)*int(t[3])
        gtplm= gtplm + tplfyt
        lstx3.insert('',"end",text="",values=(a,b,c,d,e,tplfyt))
      
        print(i[0],"0",i[1])

for i in kaytlar1:
    for t in kaytlar:
        if i[0] == t[0]:
            #print(t[1],i[0],i[1])
            break
    if i[0]!= t[0]:        
        #print(i[0],t[0])
        a=i[0]
        b=int(i[1])
        c="0"
        d=b
        e=int(i[3])
        tplfyt=int(d)*int(i[3])
        gtplm= gtplm + tplfyt
        lstx3.insert('',"end",text="",values=(a,b,c,d,e,tplfyt))
      
        print(i[0],i[1],"0")
        
lstx3.pack()
