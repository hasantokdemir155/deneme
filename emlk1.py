from tkinter import *
from tkinter import ttk
import tkinter
import sqlite3
import matplotlib.pyplot as pyp

    #def secm(lstx2):
     #   secl=lstx2.selection()
     #   print('ffffff')
     #   print(secl)

def lste():
    def lst2():
        bgln11=sqlite3.connect("emlak.db")
        kmt11=bgln11.cursor()
        
        kmt11.execute("select evkod,alckod,evdrum,kmsyon,satcad,satsfyat from satlanlar")
                     #where ognot > 50 order by ogfyat asc"  )

        kaytlar=kmt11.fetchall()
        #global lstx2

        #style= ttk.Style()

       # pn8= Tk()

        lstx2=ttk.Treeview(mytab3,height="14")

        ttk.Style().theme_use("clam")    
        ttk.Style().configure('Treeview',background='silver',foreground='green',fieldbackground="silver")
        ttk.Style().map('Treeview',background=[('selected','green')])
        
        lstx2["columns"]= ("Evkod","Alckod","Talpdrm","Kmsyon","Satcad","satsfyat")

        lstx2.column("#0",width = 2)
        lstx2.column("Evkod",width=60)
        lstx2.column("Alckod",width=60)
        lstx2.column("Talpdrm",width=80)
        lstx2.column("Kmsyon",width=110)
        
        lstx2.column("Satcad",width=110)
        lstx2.column("satsfyat",width=120)
        
        

        lstx2.heading("Evkod",text="Ev Kodu")    
        lstx2.heading("Alckod",text="Alıcıkodu")


        lstx2.heading("Talpdrm",text="Evin durumu")
                
        lstx2.heading("Kmsyon",text="Komsyon")
        lstx2.heading("Satcad",text="Satıcı Ad Soyad")
        lstx2.heading("satsfyat",text="Satış Fiyat")
        #lstx2.bind("<Return>",secm(lstx2))

        for i in kaytlar:
    
            a=i[0]
            b=i[1]
            bb=str(i[2])
            dd=i[3]
            d=i[4]
            e=i[5]
            
            lstx2.insert('',"end",text="",values=(a,b,bb,dd,d,e))
 
        lstx2.pack(padx=20,pady=30)        
    def lst1():
        bgln11=sqlite3.connect("emlak.db")
        kmt11=bgln11.cursor()
        
        kmt11.execute("select alckodu,talepstat,talepucrt,istenensemt,alcadsyad from alc")
                     #where ognot > 50 order by ogfyat asc"  )

        kaytlar=kmt11.fetchall()
        lstx1=ttk.Treeview(mytab2,height="14")

        lstx1["columns"]= ("Alckod","Talpdrm","Talpfyt","istsemt","alcadsyd")

        lstx1.column("#0",width = 2)

        lstx1.column("Alckod",width=60)
        lstx1.column("Talpdrm",width=80)
        lstx1.column("Talpfyt",width=110)
        
        lstx1.column("istsemt",width=110)
        lstx1.column("alcadsyd",width=120)
        
        
        lstx1.heading("Alckod",text="Alıcıkodu")
        lstx1.heading("Talpdrm",text="Evin durumu")
        lstx1.heading("Talpfyt",text="Fiyat")
        
        lstx1.heading("istsemt",text="Semt")
        lstx1.heading("alcadsyd",text="Alıcı Ad Soyad")

        #lstx1.tag_configure("ttk",background = "black")       
        
    
        for i in kaytlar:
    
            a=i[0]
            b=i[1]
            bb=str(i[2])
            dd=i[3]
            d=i[4]
          
            
            lstx1.insert('',"end",text="",values=(a,b,bb,dd,d))
        print(a)    
        lstx1.pack(padx=20,pady=30)

    def lst():
        bgln1=sqlite3.connect("emlak.db")
        kmt1=bgln1.cursor()
        
        kmt1.execute("select Evgrskodu,evstatu,istenenucrt,indrmmik,semt,satciadsoyad from satc")
                     #where ognot > 50 order by ogfyat asc"  )

        kaytlar=kmt1.fetchall()
        lstx=ttk.Treeview(mytab1,height="14")

        lstx["columns"]= ("Evkodu","Evdurumu","Evfyat","Opsyon","evsemt","Satcadsyd")

        lstx.column("#0",width = 2)

        lstx.column("Evkodu",width=60)
        lstx.column("Evdurumu",width=80)
        lstx.column("Evfyat",width=110)
        lstx.column("Opsyon",width=110)
        lstx.column("evsemt",width=90)
        lstx.column("Satcadsyd",width=130)
        
        
        lstx.heading("Evkodu",text="Ev kodu")
        lstx.heading("Evdurumu",text="Evin durumu")
        lstx.heading("Evfyat",text="Fiyat")
        lstx.heading("Opsyon",text="indirim Opsiyonu")
        lstx.heading("evsemt",text="Semt")
        lstx.heading("Satcadsyd",text="Satıcı Ad Soyad")

        #lstx.tag_configure("ttk",background = "black")       
        
    
        for i in kaytlar:
    
            a=i[0]
            b=i[1]
            bb=str(i[2])
            c=str(i[3])
            dd=i[4]
            d=i[5]
          
        
            lstx.insert('',"end",text="",values=(a,b,bb,c,dd,d))
        lstx.pack(padx=20,pady=30)
    pn2.destroy()    
    pn5= Tk()
    pn5.title("LİSTELER")
    pn5.geometry("700x700")
    mytab=ttk.Notebook(pn5)
    mytab.pack(pady=5)
    mytab1= ttk.Frame(mytab,width=700,height=500)
    mytab2= ttk.Frame(mytab,width=700,height=500)
    mytab3= ttk.Frame(mytab,width=700,height=500)
    mytab.add(mytab1,text="SATIŞTAKİLER Listesi")
    mytab.add(mytab2,text="ALICILAR Listesi")
    mytab.add(mytab3,text="SATILANLAR Listesi")

    Btnx=Button(mytab1,text='Satış listesi',command=lst)
    Btnx1=Button(mytab2,text='Alıcı listesi',command=lst1)
    Btnx2=Button(mytab3,text='satılan listesi',command=lst2)
    Btnx.pack()     
    Btnx1.pack()
    Btnx2.pack()

def satgrs():
    def tkla():
   
        evkod=grs.get()
        evdur=mcmb.get()
        evucr=int(grs2.get())
        evind=int(grs3.get())
        evsemt=grs4.get()
        evsatan=grs5.get()
        evadres=mytext.get(1.0,END)
        kmt.execute("insert into satc values(@p1,@p2,@p3,@p4,@p5,@p6,@p7)",(evkod,evdur,evucr,evind,evsemt,evsatan,evadres))  
        bgln.commit()
        bgln.close




     
    bgln=sqlite3.connect("emlak.db")
    kmt=bgln.cursor()

    pn3=Tk()

    etk=Label(pn3,text="EVKODU",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=36)

    etk1=Label(pn3,text="EV DURUM",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=92)

    etk2=Label(pn3,text="İSTENEN ÜCRET",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=119)

    etk3=Label(pn3,text="İNDİRİM OPSİYONU",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=139)
    etk4=Label(pn3,text="EVİN SEMTİ",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=157)

    etk44=Label(pn3,text="SATICI AD SOYAD",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=174)



    
    etk4=Label(pn3,text="EVİN ADRESİ",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=210)

    grs=Entry(pn3)

    grs.grid(row=2,column=1)

    grs.pack(padx=140,pady=50,anchor=NW)

    #grs1=Entry(pn3)
    mcmb=ttk.Combobox(pn3)
    mcmb.place(x=120,y=90)
    mcmb['values']=('SATILIK','KİRALIK')


    mcmb.current(0)

    grs2=Entry(pn3)
    grs3=Entry(pn3)
    grs4=Entry(pn3)
    grs5=Entry(pn3,width=25)
    
   # grs1.pack()
    grs2.pack()
    grs3.pack()
    grs4.pack()
    grs5.pack(padx=130)
    mytext=Text(pn3,width=30,height=4)
    mytext.pack(padx=128,pady=45)
    pn3.title("SATICI GİRİŞİ")
    pn3.geometry("380x380")

    btn13=Button(pn3,text="KAYDET",height=2,width=15,bg="GRAY",command=tkla).place(x=65,y=338)

    btn12=Button(pn3,text="KAPAT",height=2,width=15,bg="GRAY",command=pn3.destroy).place(x=185,y=338)


    pass

def alcgrs():
    def tkla1():
   
        alankod=grss1.get()

        evalan=grss2.get()
        alanucr=int(grss3.get())
        alanevdur=mcmb1.get()
        alansemt=grss5.get()
       
        kmt.execute("insert into alc values(@p1,@p2,@p3,@p4,@p5)",(alankod,alanevdur,alanucr,alansemt,evalan))  
        bgln.commit()
        bgln.close





    
    bgln=sqlite3.connect("emlak.db")
    kmt=bgln.cursor()
    
    pn4=Tk()

    pn4.title("ALICI GİRİŞİ")
    pn4.geometry("500x550")

    etkk=Label(pn4,text="ALICIKODU",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=40)

    etkk1=Label(pn4,text="ALICI AD SOYAD",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=92)

    etkk2=Label(pn4,text="ÜCRET OPSİYONU",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=112)

    etkk3=Label(pn4,text="İSTENEN SEMT",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=129)
    etkk4=Label(pn4,text="İSTENEN EV DURUMU",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=152)
    
    grss1=Entry(pn4,width=20)
    grss2=Entry(pn4)
    grss3=Entry(pn4)
    mcmb1=ttk.Combobox(pn4)
    mcmb1.place(x=185,y=152)
    mcmb1['values']=('SATILIK','KİRALIK')


    mcmb1.current(0)
    #grss4=Entry(pn4)
    grss5=Entry(pn4)

    grss1.pack(padx=135,pady=37)
    grss2.pack(padx=185)
    grss3.pack(padx=185)
  

    #grss4.pack(padx=185)
    grss5.pack(padx=185)

    

    btn14=Button(pn4,text="KAYDET",height=2,width=15,bg="GRAY",command=tkla1).place(x=65,y=320)

    btn15=Button(pn4,text="KAPAT",height=2,width=15,bg="GRAY",command=pn4.destroy).place(x=185,y=320)


   


def satln():
    def sats():
        evkod1=mcmb1.get()
        alckod=mcmb2.get()
        evstat=grss3   
        evkom=int(grsss6.get())
        evsatc=mcmb3.get()
        evalc=mcmb4.get()
        evucr=int(grsss7.get())
        kmt=bgln1.cursor()
        kmt.execute("insert into satlanlar values(@p1,@p2,@p3,@p4,@p5,@p6,@p7)",(evkod1,alckod,evstat,evkom,evsatc,evalc,evucr))  
        bgln1.commit()
        bgln1.close    
        print('aaaaaaaaaaaa')   
               
      
    pn6=Tk()

    pn6.title("SATILAN GİRİŞİ")
    pn6.geometry("490x450")
    etkkk=Label(pn6,text="SATILAN EV KODU",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=36)

    etkkk1=Label(pn6,text="ALICI KODU",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=92)

    etkkk2=Label(pn6,text="EV STATÜ",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=117)

    etkkk3=Label(pn6,text="SATICI ADSOYAD",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=141)
    etkkk44=Label(pn6,text="ALICI ADSOYAD",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=159)

    etkkk4=Label(pn6,text="KOMİSYON ÜCRETİ",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=190)

    etkkk5=Label(pn6,text="ÜCRET",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=208)

    bgln1=sqlite3.connect("emlak.db")

    kmt1=bgln1.cursor()
    kmt1.execute("select Evgrskodu from satc group by Evgrskodu")
                     #where ognot > 50 order by ogfyat asc"  )

    kaytlar=kmt1.fetchall()

    
    mcmb1=ttk.Combobox(pn6,width=16)
    mcmb1.place(x=186,y=36)
    mcmb1['values']=kaytlar
    mcmb1.current(0)    

    bgln1=sqlite3.connect("emlak.db")
    kmt1=bgln1.cursor()
    kmt1.execute("select alckodu from alc group by alckodu")
    kaytlar=kmt1.fetchall()
    mks=[]
    mcmb2=ttk.Combobox(pn6,width=16)
    mcmb2.place(x=186,y=92)
    mcmb2['values']=kaytlar
    mcmb2.current(0)    

    kmt1=bgln1.cursor()
    kmt1.execute("select satciadsoyad from satc group by satciadsoyad")
    kaytlar=kmt1.fetchall()
    
    mcmb3=ttk.Combobox(pn6,width=16)
    mcmb3.place(x=186,y=141)
    mcmb3['values']=kaytlar
    mcmb3.current(0)    

    kmt1=bgln1.cursor()
    kmt1.execute("select alcadsyad from alc group by alcadsyad")
    kaytlar=kmt1.fetchall()
    for i in kaytlar:
        mks.append(i)
    print(kaytlar)

    mcmb4=ttk.Combobox(pn6,width=16)
    mcmb4.place(x=186,y=159)
    
    mcmb4['values']=kaytlar
    
    mcmb4.current(0)
        
   # grsss1=Entry(pn6,width=20)
   # grsss2=Entry(pn6)

    mcmb=ttk.Combobox(pn6,width=16)
    mcmb.place(x=186,y=120)
    mcmb['values']=('SATILIK','KİRALIK')
   # mcmb(pady=15)

    mcmb.current(0)
    grss3=mcmb.get()
    #grsss3=Entry(pn6)

    #grsss4=Entry(pn6)
   # grsss5=Entry(pn6)
    grsss6=Entry(pn6)
    grsss7=Entry(pn6)
    grsss7.place(x=183,y=215)
    grsss6.pack(pady=190)
    
    
    #grsss1.pack(padx=135,pady=32)
    #grsss2.pack(padx=185,pady=57)
    #grsss3.pack(padx=185,pady=3)
    #grsss4.pack(padx=185,pady=71)
    #grsss5.pack(padx=185)
    #grsss6.pack(padx=185,pady=165)
    #grsss7.pack(padx=185)
  

    btn16=Button(pn6,text="KAYDET",height=2,width=15,bg="GRAY",command=sats).place(x=65,y=320)

    btn17=Button(pn6,text="KAPAT",height=2,width=15,bg="GRAY",command=pn6.destroy).place(x=185,y=320)








    

    pass



        
pn2=tkinter.Tk()
ttk.Style().theme_use("clam")    
ttk.Style().configure('Treeview',background='silver',foreground='green',fieldbackground="silver")
ttk.Style().map('Treeview',background=[('selected','green')])


pn2.title("EMLAK OTOMASYON")
pn2.geometry("500x500")

btn11=Button(pn2,text="SATILIK/KİRALIK EV",height=5,width=15,bg="YELLOW",command=satgrs).place(x=140,y=140)

btn21=Button(pn2,text="SATIŞ GİRİŞİ",height=5,width=15,bg="GREEN",command=satln).place(x=140,y=240)

btn31=Button(pn2,text="ALICI KAYDI",height=5,width=15,bg="aqua",command=alcgrs).place(x=140,y=340)

btn41=Button(pn2,text="LİSTELER",height=18,width=15,bg="PURPLE",command=lste).place(x=259,y=140)

btn51=Button(pn2,text="ÇIKIŞ",height=2,width=35,bg="gray",command=pn2.destroy).place(x=140,y=435)

