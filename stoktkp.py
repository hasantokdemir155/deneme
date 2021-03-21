from tkinter import *
import sqlite3
from tkinter import ttk



def gstokdok():
     kmtl=bglnl.cursor()
     kmt2=bglnl.cursor()
#kmtl.execute("drop view dnmlx1")
     #kmtl.execute("CREATE VIEW dnmlx  as select sum (tutar)  ttr,msterkod,odenen,iskod from islemsats group by iskod")
#kmtl.execute("select  amalad,sum(amaladet),sum(mktar),amalkod from islemals,islemsats where islemals.amalkod=islemsats.malkod")
     kmt2.execute("select  amalad,sum(amaladet),amalkod,amalfyat from islemals group by amalkod")
     kmtl.execute("select  malad,sum(mktar),malkod from islemsats group by malkod")

     kaytlar=kmtl.fetchall()
     kaytlar1=kmt2.fetchall()

     
     
     for rc in lstx3.get_children():
          lstx3.delete(rc)
     for rc1 in lstx31.get_children():
          lstx31.delete(rc1)
     #lstx3.destroy()     
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
                 lstx31.insert('',"end",text="",values=(a,b,c,d,e,tplfyt))
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
                  lstx31.insert('',"end",text="",values=(a,b,c,d,e,tplfyt))
      
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
                  lstx31.insert('',"end",text="",values=(a,b,c,d,e,tplfyt))
      
                  print(i[0],i[1],"0")
        
     lstx31.pack(padx=1,pady=65)
     etk2=Label(stokekr,text="Genel stok tutar",font=("Bold",12)
          #width= 20,
     ).place(x=320,y=465)
     etk21=Label(stokekr,text=str(gtplm),font=("Bold",12)
          #width= 20,
     ).place(x=515,y=465)
     pass
def stokdok():
     b=mcmb4.get()   
    
     for rc in lstx3.get_children():
          lstx3.delete(rc)
     for rc1 in lstx31.get_children():
          lstx31.delete(rc1)
         
     kmtl=bglnl.cursor()
     kmtl.execute("select  amalad,amaladet,iskod,tedrkkod from islemals where  amalad like '%" + mcmb4.get()+"%'")  
     kaytlar=kmtl.fetchall()

     
     for i in kaytlar:
         a=i[0]
         bb=0 
         b=i[1]
         c=i[2]
         d=i[3]
         print(a,b,c,d)    
          
         lstx3.insert('',"end",text="",values=(a,bb,b,c,d))

          

     kmtl=bglnl.cursor()
     kmtl.execute("select  malad,mktar,iskod,msterkod from islemsats where  malad like '%" + mcmb4.get()+"%'")  
     kaytlar=kmtl.fetchall()

     
     for i in kaytlar:
         a=i[0]
         bb=i[1]
         b=0
         c=i[2]
         d=i[3]
            
          
         lstx3.insert('',"end",text="",values=(a,bb,b,c,d))

     print(a,b,c,d) 
     lstx3.pack(padx=5,pady=65)
     
stokekr=Tk()
stokekr.geometry("800x500")
frm=Frame(stokekr,width=250,height=25)
frm.place(x=5,y=30)

frm1=Frame(stokekr,width=350,height=25)
frm1.place(x=265,y=37)
bglnl=sqlite3.connect("onmuhasebe.db")

kmt1=bglnl.cursor()
kmt1.execute("select stokad from stokkart group by stokad")
kaytlar=kmt1.fetchall()


    
mcmb4=ttk.Combobox(stokekr,width=16)
mcmb4.place(x=276,y=65)
mcmb4['values']=kaytlar
print(mcmb4['values'])
mcmb4.current(0)    


Btnx=Button(stokekr,text='STOK DÖKÜM',command=stokdok).place(x=420,y=57)

Btnx=Button(stokekr,text='GENEL STOK DÖKÜM',command=gstokdok).place(x=540,y=57)

lstx31=ttk.Treeview(frm1,height="14")

ttk.Style().theme_use("clam")    
ttk.Style().configure('Treeview',background='silver',foreground='green',fieldbackground="silver")
ttk.Style().map('Treeview',background=[('selected','green')])
        
lstx31["columns"]= ("stokad","satlan","alnan","kalan","fyat","stoktutar")

lstx31.column("#0",width = 2)
lstx31.column("stokad",width=75)
lstx31.column("satlan",width=76)
lstx31.column("alnan",width=88)
lstx31.column("kalan",width=88)
lstx31.column("fyat",width=88)

lstx31.column("stoktutar",width=88)

        
        

lstx31.heading("stokad",text="stokadı")    
lstx31.heading("satlan",text="alınan adet")
lstx31.heading("alnan",text="satılan adet")
lstx31.heading("kalan",text="kalan adet")
lstx31.heading("fyat",text="alım fiyatı")

lstx31.heading("stoktutar",text="stok tutarı")


lstx3=ttk.Treeview(frm,height="14")

ttk.Style().theme_use("clam")    
ttk.Style().configure('Treeview',background='silver',foreground='green',fieldbackground="silver")
ttk.Style().map('Treeview',background=[('selected','green')])
        
lstx3["columns"]= ("stokad","satlan","alnan","islemkod","musterad")

lstx3.column("#0",width = 2)
lstx3.column("stokad",width=75)
lstx3.column("satlan",width=60)
lstx3.column("alnan",width=60)

lstx3.column("islemkod",width=75)  
lstx3.column("musterad",width=105)  
        
        

lstx3.heading("stokad",text="stokadı")    
lstx3.heading("satlan",text="satılan adet")
lstx3.heading("alnan",text="alınan adet")

lstx3.heading("islemkod",text="işlem kod")
lstx3.heading("musterad",text="müşteri adı")
                

