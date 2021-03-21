from tkinter import *
from tkinter import ttk
#def ogrnc():
   # ekr.ekrgrn()
    #ekr.ekrgrs()
from time import sleep




import sqlite3
import matplotlib.pyplot as pyp
import pandas






def lst4():
    def sonc():
      
        
        dstl=lkste.curselection()
          
        dst=lkste.get(dstl)
        
        kaytlar=kmt1.fetchall()   
        kmt1.execute("select * from ogrnci,snflar where ogrnci.ogno=snflar.oggno and snflar.snf like '%"+ dst+"%' order by ogno")            
        
        lstx2.delete(*lstx2.get_children())    
        for i in kaytlar:
    
            a=i[0]
            b=i[1]
            bb=i[2]
            dd=i[6]
        
  
            lstx2.insert('',"end",text="",values=(a,b,bb,dd))
        
        

    

    bgln1=sqlite3.connect("okul.db")
    kmt1=bgln1.cursor()

    kmt1.execute("select * from snflar group by  snf")
    frm=LabelFrame(mytab3,text="Mevcut sınıflar",width=50,height=15)
    frm.place(x=390,y=120)
    
    
    kaytlar=kmt1.fetchall()

    lkste=Listbox(frm,width= 10,height=5)
    
    for i in kaytlar:
       
      
         lkste.insert(1,i[1])
           
    
    lkste.pack(padx=10,pady=30)

    ttk.Style().theme_use("clam")
    ttk.Style().configure('Treeview',background='silver',foreground='green',fieldbackground="silver")
    ttk.Style().map('Treeview',background=[('selected','purple')])  

    frm1=LabelFrame(mytab3,text="Sınıf Listesi",width=50,height=15)
    frm1.place(x=20,y=5)
    

    lstx2=ttk.Treeview(frm1,show="headings",height="14") 
        
    
       
    lstx2["columns"]= ("ogrno","ogradı","ogrsoyad","ogrsnf")

    lstx2.column("#0",width = 2)
    lstx2.column("ogrno",width=40)
    lstx2.column("ogradı",width=40)
    lstx2.column("ogrsoyad",width=90)
    lstx2.column("ogrsnf",width=80)

    lstx2.heading("ogrno",text="Öğrencino")
    lstx2.heading("ogradı",text="Öğrenciadı")
    lstx2.heading("ogrsoyad",text="Öğrencisoyadı")
    lstx2.heading("ogrsnf",text="Öğrencisınıf")
    lstx2.tag_configure("ttk",background = "black")       

    lstx2.pack(padx=10,pady=20)
    
 
    btn8=Button(mytab3,text="bas bakalım",command=sonc).place(x=440,y=420)
    
    
    
   
    
def lst3():
    bgln1=sqlite3.connect("okul.db")
    kmt1=bgln1.cursor()
    kmt1.execute("select * from ogrnci,snflar where ogrnci.ogno=snflar.oggno order by ogno asc")
                     #where ognot > 50 order by ogfyat asc"  )
    
    kaytlar=kmt1.fetchall()
    yıllar=[]
    sayılar=[]
    for i in kaytlar:

        yıllar.append(i[0])
        sayılar.append(i[3])
                    
        
    #yıllar=[2001,2002,2003,2004,2005,2006,2007]
    #sayılar=[12,14,15,16,17,18,19]
    pyp.plot(yıllar,sayılar)
    pyp.show()
  
def lst1():
           
    bgln1=sqlite3.connect("okul.db")
    kmt1=bgln1.cursor()
        #var=intVar()
        
        #ogno,ogad,osoyad,ogfyat,ognot
    kmt1.execute("select * from ogrnci,snflar where ogrnci.ogno=snflar.oggno order by ogno asc")
                     #where ognot > 50 order by ogfyat asc"  )

    kaytlar=kmt1.fetchall()
    lstx=ttk.Treeview(mytab1,height="14")

    lstx["columns"]= ("ogrno","ogradı","ogrsoyad","ogrsnf","ogrfyat","ogrnot")

    lstx.column("#0",width = 2)

    lstx.column("ogrno",width=40)
    lstx.column("ogradı",width=40)
    lstx.column("ogrsoyad",width=90)
    lstx.column("ogrsnf",width=80)
    lstx.column("ogrfyat",width=90)
    lstx.column("ogrnot",width=110)
        
        
    lstx.heading("ogrno",text="Öğrencino")
    lstx.heading("ogradı",text="Öğrenciadı")
    lstx.heading("ogrsoyad",text="Öğrencisoyadı")
    lstx.heading("ogrsnf",text="Öğrencisınıf")
    lstx.heading("ogrfyat",text="Öğrenci notu")
    lstx.heading("ogrnot",text="Öğrenci ücreti")

    lstx.tag_configure("ttk",background = "black")       
        
    s = 0
    tp = 0
    tpuc = 0 
    for i in kaytlar:
    
        a=i[0]
        b=i[1]
        bb=i[2]
        c=i[6]
        dd=i[3]
        d=str(i[4])
        e=str(i[3])
        
        tp= tp + int(d)
        tpuc=tpuc+ int(e)
        s = s + 1
        lstx.insert('',"end",text="",values=(a,b,bb,c,d,e))
    ort =tp/s
    ortuc=tpuc/s
    ort=round(ort,3)
    ortuc=round(ortuc,3)

    ort1=Label(pn3,text=float(ort),font=("Bold",10)).place(x=380,y=320)

    ort2=Label(pn3,text="Not ortalaması",font=("Bold",10)).place(x=280,y=320)

    ort21=Label(pn3,text=ortuc,font=("Bold",10)).place(x=190,y=320)
    ort22=Label(pn3,text="Ücret ortalaması",font=("Bold",10)).place(x=85,y=320)
      #print(a,b)


    lstx.pack(padx=20,pady=30)
          
def lst2():
    
    bgln1=sqlite3.connect("okul.db")
    kmt1=bgln1.cursor()
        #var=intVar()
        
        #ogno,ogad,osoyad,ogfyat,ognot
    kmt1.execute("select * from snavlar")
                     #where ognot > 50 order by ogfyat asc"  )
    kaytlar=kmt1.fetchall()
    lstx1=ttk.Treeview(mytab2,height="10")

    lstx1["columns"]= ("ognoa","turkcenot","matmanot","fennot","sosnot")

    lstx1.column("#0",width = 2)

    lstx1.column("ognoa",width=40)
    lstx1.column("turkcenot",width=90)
    lstx1.column("matmanot",width=80)
    lstx1.column("fennot",width=90)
    lstx1.column("sosnot",width=110)
        
        
    lstx1.heading("ognoa",text="Öğrencino")
    lstx1.heading("turkcenot",text="Türkçe")
    lstx1.heading("matmanot",text="Matematik")
    lstx1.heading("fennot",text="Fen Bilgisi")
    lstx1.heading("sosnot",text="Sosyal")

    #tag_configure(lstx1,foreground = "black")       
        
    #s = 0
    #tp = 0
    #tpuc = 0 
    for i in kaytlar:
    
        a=i[0]
        b=i[1]
        c=i[2]
        d=str(i[3])
        e=str(i[4])
     #   tp= tp + int(e)
      #  tpuc=tpuc+ int(d)
      #  s = s + 1
        lstx1.insert('',"end",text="",values=(a,b,c,d,e))

  
    lstx1.pack(padx=20,pady=5)
     


def ekrgrn():
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
    
 #   kmt.execute(create table if not exists ogrnci(ogno integer,ogad text,osoyad text,ogfyat integer,ognot integer)")
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

def ekrlst():
    def lst():
  
        btn14=Button(pn3,text="öğrenci listesi",width=20,bg="gray",command=lst1).place(x=30,y=420)
        btn15=Button(pn3,text="Öğrenci notları",width=20,bg="gray",command=lst2).place(x=130,y=420)       
        
        btn16=Button(pn3,text="Öğrenci not grafiği",width=25,bg="gray",command=lst3).place(x=210,y=420) 
        btn17=Button(pn3,text="Sınıf Listeleri",width=25,bg="gray",command=lst4).place(x=300,y=420)

        
    global pn3
    global mytab1
    global mytab2
    global mytab3
    global dst
    global dstl
   

    pn3= Tk()
    pn3.title("öğrenci liste ekranı")
    pn3.geometry("500x500")
    mytab=ttk.Notebook(pn3)
    mytab.pack(pady=5)
    mytab1= ttk.Frame(mytab,width=500,height=500)
    mytab2= ttk.Frame(mytab,width=500,height=500)
    mytab3= ttk.Frame(mytab,width=500,height=500)
    mytab.add(mytab1,text="Öğrenci Listesi")
    mytab.add(mytab2,text="Öğrenci Notları")
    mytab.add(mytab3,text="Öğrenci Sınıf Listeleri")
    lst()
    

def snavuyg():
    def snavdegrln():
        def sınavbasla():
            dsnv1=lkstexx.curselection()
            dsnv=lkstexx.get(dsnv1)

                          
            
            dsx1=lkstexx1.curselection()
            dsx=lkstexx1.get(dsx1)
            
           
            #print(dsnv,"2")
            
            kmt.execute("select * from ogrsnav  where ogrsnv like '%"+ dsnv+"%' and  ogrders like '%"+ dsx+"%'")
            kmtl.execute("select * from snav  where snavkod like '%"+ dsnv+"%' and  snavders like '%"+ dsx+"%'") 
            myprog=ttk.Progressbar(frmprgrs,orient=HORIZONTAL,length=230,mode='determinate',value=1)
            myprog.pack(padx=40)
            k= 0   
            while k < 230:
                sleep(0.0008)
                k= k +2
                myprog['value']=k
                
            
            kaytlar=kmt.fetchall()
            kayıtlar1=kmtl.fetchall()

            #print(kayıtlar1)
            for i in kayıtlar1:
       
                snvcvp= i[2] 

            pn7= Tk()
            pn7.title("SINAV SONUÇLARI ")
            pn7.geometry("450x450")
            
            lstx7=ttk.Treeview(pn7,height="10")

            lstx7["columns"]= ("ognora","ad","soyad","dogrus","not")

            lstx7.column("#0",width = 2)

            lstx7.column("ognora",width=40)
            lstx7.column("ad",width=90)
            lstx7.column("soyad",width=80)
            lstx7.column("dogrus",width=90)
            lstx7.column("not",width=110)
        
        
            lstx7.heading("ognora",text="Öğrencino")
            lstx7.heading("ad",text="Öğrenci Ad")
            lstx7.heading("soyad",text="Öğrenci Soyad")
            lstx7.heading("dogrus",text="Doğrusayı")
            lstx7.heading("not",text="SınavNot")
          
            for i in kaytlar:
       
                ogrcvp= i[3] 

                dgru=0
                mi=0

                while mi <= 24:

                    if snvcvp[mi]== ogrcvp[mi]:
                        dgru = dgru + 1
                    mi += 1    
                z=str(i[0])
                
                kmt.execute("select * from ogrnci where ogno =("+z +") ") 
                kaytlar=kmt.fetchall()
                
                for i in kaytlar:
                    
                    #print(i[0],i[1],i[2],dgru,dgru*4)
                    p=i[0]
                    q=i[1]
                    r=i[2]
                    s=dgru
                    t=dgru*4


                    lstx7.insert('',"end",text="",values=(p,q,r,s,t))

  
            lstx7.pack(padx=20,pady=5)

          

            
                                    
            pass

     
        bgln=sqlite3.connect("okul.db")
        kmt=bgln.cursor()   
        kmtl=bgln.cursor() 
        
        kmt.execute("select * from snav group by snavkod,snavders")

        
        frmxx=LabelFrame(mytab31,text="Mevcut sınavlar",width=50,height=95)
        frmxx.place(x=330,y=110)
    
    
        kaytlar=kmt.fetchall()
        item=[]
        lkstexx=Listbox(frmxx,width= 10,height=5,exportselection=0)
        lkstexx1=Listbox(frmxx,width= 10,height=5,exportselection=0)
        lkstexx.activate(1)
        
        m=1
        for i in kaytlar:
       
              
             lkstexx.insert(m,i[0])
             lkstexx1.insert(m,i[1])
             m=m+1
         

        lkstexx.pack(padx=10,pady=30)
        #mcmb1.pack()
        lkstexx1.pack(padx=10,pady=30)
        bgln.commit()
        bgln.close
        bgln=sqlite3.connect("okul.db")
        kmt=bgln.cursor()   
      
        lkstexx.selection_set(first=1)
        lkstexx1.selection_set(first=1)
      
        kaytlar=kmt.fetchall()
          
        btn5xx2=Button(mytab31,text="SINAVI BAŞLAT",height=1,width=15,bg="BLUE",command=sınavbasla).place(x=340,y=420)

        
    def snvkayt():
        snavkod=grsn1.get()
        snavders=grsn2.get()
        sorsays=grsn3.get()
        snavcevapanah=grsn4.get()

        kmt.execute("insert into snav values(@p1,@p2,@p3,@p4)",(snavkod,snavders,snavcevapanah,sorsays))  
        bgln.commit()
        bgln.close
    def ogrsnvkayt():
        ogrsno=int(grso1.get())
        ogrders=grso2.get()
        ogrsnv=grso3.get()
        ogrcvp=grso4.get()

        kmt.execute("insert into ogrsnav values(@p1,@p2,@p3,@p4)",(ogrsno,ogrders,ogrsnv,ogrcvp))  
        bgln.commit()
        bgln.close
     

    
    bgln=sqlite3.connect("okul.db")
    kmt=bgln.cursor()            
    pn33=Tk()
    mytab=ttk.Notebook(pn33)
    mytab.pack(pady=5)
    mytab11= ttk.Frame(mytab,width=500,height=500)
    mytab21= ttk.Frame(mytab,width=500,height=500)
    mytab31= ttk.Frame(mytab,width=500,height=500)
    
    mytab.add(mytab11,text="Sınav Girişi")
    mytab.add(mytab21,text="Öğrenci Cevapları")
    mytab.add(mytab31,text="Sınav Sonuç")

    frmprgrs=LabelFrame(mytab31,text="Mevcut durum",width=220,height=25)
    frmprgrs.place(x=90,y=65)

   

    btn511=Button(mytab31,text="SINAV değerlendirme",height=5,width=25,bg="GREEN",command=snavdegrln).place(x=140,y=180)
    
    setk=Label(mytab11,text="SINAVKODU",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=35)

    setk1=Label(mytab11,text="DERSADI",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=85)

    setk1=Label(mytab11,text="SORU SAYISI",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=105)

    setk2=Label(mytab11,text="CEVAP ANAHTAR",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=125)

    grsn1=Entry(mytab11)
    grsn2=Entry(mytab11)
    grsn3=Entry(mytab11)
    grsn4=Entry(mytab11,width=30)

    grsn1.pack(pady=35)
    grsn2.pack()
    grsn3.pack(padx=165)
    grsn4.pack(padx=165)    
    btn41=Button(mytab11,text="SINAVI KAYDET",height=5,width=25,bg="GREEN",command=snvkayt).place(x=175,y=180)


    setkO=Label(mytab21,text="ÖĞRENCİNO",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=35)

    setkO1=Label(mytab21,text="DERSADI",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=85)

    setkO2=Label(mytab21,text="SINAVKODU",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=105)
    
    setkO3=Label(mytab21,text="CEVAPLAR",font=("Bold",10)
          #width= 20,
    ).place(x=25,y=125)
    
    grso1=Entry(mytab21)
    grso2=Entry(mytab21)
    grso3=Entry(mytab21)
    grso4=Entry(mytab21,width=30)

    grso1.pack(pady=35)
    grso2.pack()
    grso3.pack()
    grso4.pack(padx=165)

    btn51=Button(mytab21,text="ÖĞRENCİ SINAVI KAYDET",height=5,width=25,bg="GREEN",command=ogrsnvkayt).place(x=175,y=180)
    
    pass

global dsx
global dsnv
global dsnv1
global dsx1

ttk.Style().theme_use("clam")
ttk.Style().configure('Treeview',background='silver',foreground='green',fieldbackground="silver")
ttk.Style().map('Treeview',background=[('selected','purple')])

pn2=Tk()

pn2.title("ÖĞRENCİ İŞLERİ")
pn2.geometry("500x500")

btn11=Button(pn2,text="ÖĞRENCİ KAYDI",height=5,width=15,bg="red",command=ekrgrn).place(x=40,y=180)

btn21=Button(pn2,text="ÇIKIŞ",height=5,width=15,bg="blue",command=pn2.destroy).place(x=240,y=180)

btn31=Button(pn2,text="ÖĞRENCİ LİSTELE",height=5,width=15,bg="aqua",command=ekrlst).place(x=140,y=180)

btn41=Button(pn2,text="SINAV UYGULAMASI",height=5,width=15,bg="PURPLE",command=snavuyg).place(x=355,y=180)

