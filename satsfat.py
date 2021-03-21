from tkinter import *
import sqlite3
from tkinter import ttk


def fatraols():

     gg=[]     
     info=lstx2.get_children()
     kmt=bglnl.cursor()
     for i in info:
          info2=lstx2.set(i)
          
          print([*info2.values()])
          gg=[*info2.values()]
          print(gg[0],gg[1],gg[2])
              
          iskod=gg[0]
          malkod=gg[1]
          malad=gg[2]
          mktar=int(gg[3])
          satfyat=int(gg[4])
          msterkod=mcmb3.get() 
          odenen=int(grs13.get())
          tutar=mktar*satfyat
          kmt.execute("insert into islemsats values(@p1,@p2,@p3,@p4,@p5,@p6,@p7,@p8)",
                      (iskod,malkod,malad,mktar,satfyat,msterkod,odenen,tutar))
     bglnl.commit()
     bglnl.close
          
          
def fatraaktar():
        
     #a=grs.get()
     #print(a)
    
     #kmtl=bglnl.cursor()
     #kmt1.execute("select stokkod from stokkart where stokad like '%" + mcmb4.get()+"%'")
     #kaytlar= kmtl.fetchall()
     #kmt1.execute("select * from ogrnci,snflar where ogrnci.ogno=snflar.oggno and snflar.snf like '%"+ dst+"%' 

     zzind=zz.index(mcmb4.get())    
     
     
     a=grs11.get()
     b=zz1[zzind]
     bb=mcmb4.get()
     c=int(grs14.get())
     d=int(grs15.get())
     dd=d*c

     #if grs != " " :      

     lstx2.insert('',"end",text="",values=(a,b,bb,c,d,dd))
     grs11.delete(0,END)
     
     
     grs14.delete(0,END)
     grs15.delete(0,END)
     
     lstx2.pack(padx=25,pady=125)

def fatrackar():
     x=lstx2.selection()[0]
     lstx2.delete(x)
    
satsekr=Tk()
satsekr.geometry("800x500")

frm=Frame(satsekr,width=750,height=25)
frm.place(x=10,y=30)

frm1=Frame(satsekr,width=750,height=25)
frm1.place(x=10,y=80)

bgln11=sqlite3.connect("onmuhasebe.db")
kmt11=bgln11.cursor()


etk=Label(frm,text="İŞLEMKODU",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=36)

etk=Label(frm,text="Müşteri adı",font=("Bold",10)
          #width= 20,
    ).place(x=290,y=36)






etk=Label(frm,text="Ürün kodu",font=("Bold",10)
          #width= 20,
   ).place(x=3,y=105)

#etk=Label(frm,text="Ürün adı",font=("Bold",10)
          #width= 20,
#    ).place(x=145,y=105)
#etk=Label(frm,text="Ürün miktar",font=("Bold",10)
          #width= 20,
#    ).place(x=295,y=105)
#etk=Label(frm,text="Satışfiyat",font=("Bold",10)
          #width= 20,
#    ).place(x=475,y=105)

grs=Label(satsekr,text="işlemkod").place(x=40,y=1)
grsx=Label(satsekr,text="ödenen").place(x=145,y=1)
grs12=Label(satsekr,text="müşteri ad").place(x=280,y=1)
grs21=Label(satsekr,text="Ürün adı",font=("Bold",10)
          #width= 20,
   ).place(x=20,y=55)

grs22=Label(satsekr,text="Ürün miktar",font=("Bold",10)
          #width= 20,
   ).place(x=135,y=55)
grs23=Label(satsekr,text="Satış fiyat",font=("Bold",10)
          #width= 20,
   ).place(x=255,y=55)


grs11=Entry(frm)
grs11.grid(row=0,column=1)

grs13=Entry(frm)
grs13.grid(row=0,column=4)


#grs113=Entry(frm1)
#grs113.grid(row=0,column=1)

grs14=Entry(frm1)
grs14.grid(row=0,column=2)

grs15=Entry(frm1)
grs15.grid(row=0,column=3)


#grs1=Entry(frm,width=10)
#grs1.grid(row=3,column=0)

#grs2=Entry(frm,width=15)
#grs2.grid(row=3,column=2)



#grs3=Entry(frm,width=15)
#grs3.grid(row=3,column=3)
#grs4=Entry(frm,width=15)
#grs4.grid(row=0,column=4)

Btnx=Button(satsekr,text='Faturaya aktar',command=fatraaktar).place(x=420,y=77)
Btnx1=Button(satsekr,text='Faturadan çıkar',command=fatrackar).place(x=520,y=77)
Btnx2=Button(satsekr,text='Fatura oluştur',width=25,command=fatraols).place(x=475,y=25)

bglnl=sqlite3.connect("onmuhasebe.db")
kmt1=bglnl.cursor()
kmt1.execute("select musterad from msteri group by musterad")
kaytlar=kmt1.fetchall()
    
mcmb3=ttk.Combobox(satsekr,width=16)
mcmb3.place(x=276,y=27)
mcmb3['values']=kaytlar
mcmb3.current(0)    

kmt1=bglnl.cursor()
kmt1.execute("select stokad,stokkod from stokkart group by stokad")
kaytlar=kmt1.fetchall()

zz=[]
zz1=[]

for i in kaytlar:
     zz.append(i[0])
     zz1.append(i[1])

    
mcmb4=ttk.Combobox(frm1,width=16)
mcmb4.grid(row=0,column=1)
mcmb4['values']=zz
mcmb4.current(0)    


lstx2=ttk.Treeview(satsekr,height="14")

ttk.Style().theme_use("clam")    
ttk.Style().configure('Treeview',background='silver',foreground='green',fieldbackground="silver")
ttk.Style().map('Treeview',background=[('selected','green')])
        
lstx2["columns"]= ("iskod","Malkod","Malad","Miktar","Satfyat","tutar")

lstx2.column("#0",width = 2)
lstx2.column("iskod",width=45)
lstx2.column("Malkod",width=60)
lstx2.column("Malad",width=80)
lstx2.column("Miktar",width=80)
        
lstx2.column("Satfyat",width=90)
lstx2.column("tutar",width=110)
        
        

lstx2.heading("iskod",text="İşlemkod")    
lstx2.heading("Malkod",text="Ürünkod")


lstx2.heading("Malad",text="Ürünadı")
                
lstx2.heading("Miktar",text="Miktarı")
lstx2.heading("Satfyat",text="Satış fiyat")
lstx2.heading("tutar",text="Tutarı")

#lstx2.pack()




