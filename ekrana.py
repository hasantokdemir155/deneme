from tkinter import *
from tkinter import ttk
#def ogrnc():
   # ekr.ekrgrn()
    #ekr.ekrgrs()



import sqlite3

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
        


        bgln1=sqlite3.connect("okul.db")
        kmt1=bgln1.cursor()
        #var=intVar()
        
        #ogno,ogad,osoyad,ogfyat,ognot
        kmt1.execute("select * from ogrnci")
                     #where ognot > 50 order by ogfyat asc"  )
        kaytlar=kmt1.fetchall()

        frm=LabelFrame(pn3,text="Listelenmek istenen değerler",width=250,height=120)
        frm.place(x=44,y=355)
        var=StringVar()
        var1=StringVar()
        var2=StringVar()
        var3=StringVar()

        ck=  Checkbutton(frm,text="Öğrenci No",variable=var,onvalue="ON",offvalue="OFF")


        ck1=  Checkbutton(frm,text="Öğrenci adı",variable=var1,onvalue="ON",offvalue="OFF")
        ck2=  Checkbutton(frm,text="Öğrenci soyadı",variable=var2,onvalue="ON",offvalue="OFF")
        ck3=  Checkbutton(frm,text="Öğrenci Ücreti",variable=var3,onvalue="ON",offvalue="OFF")
#ck1= Checkbutton(frm,text="Öğrenci Adı")
#ck2= Checkbutton(frm,text="ÖğrenciSoyadı")
#ck3= Checkbutton(frm,text="Öğrenci Not")
        ck.deselect()
        ck.place(x=30,y=15)
        ck1.place(x=30,y=35)   #ck3.pack()
        ck2.place(x=30,y=55)
        ck3.place(x=30,y=75)



        
        lstx=ttk.Treeview(pn3,height="14")

        lstx["columns"]= ("ogrno","ogradı","ogrsoyad","ogrfyat","ogrnot")

        lstx.column("#0",width = 2)

        lstx.column("ogrno",width=40)
        lstx.column("ogradı",width=90)
        lstx.column("ogrsoyad",width=80)
        lstx.column("ogrfyat",width=90)
        lstx.column("ogrnot",width=110)
        
        
        lstx.heading("ogrno",text="Öğrencino")
        lstx.heading("ogradı",text="Öğrenciadı")
        lstx.heading("ogrsoyad",text="Öğrencisoyadı")
        lstx.heading("ogrfyat",text="Öğrenci ücreti")
        lstx.heading("ogrnot",text="Öğrenci notu")

        lstx.tag_configure("ttk",foreground = "black")       
        
        s = 0
        tp = 0
        tpuc = 0 
        for i in kaytlar:
    
            a=i[0]
            b=i[1]
            c=i[2]
            d=str(i[3])
            e=str(i[4])

            tp= tp + int(e)
            tpuc=tpuc+ int(d)
            s = s + 1    
            
            lstx.insert('',"end",text="",values=(a,b,c,d,e))
        ort =tp/s
        ortuc=tpuc/s
        ort=round(ort,3)
        ortuc=round(ortuc,3)

        ort1=Label(pn3,text=float(ort),font=("Bold",10)).place(x=380,y=320)
        ort2=Label(pn3,text="Not ortalaması",font=("Bold",10)).place(x=280,y=320)

        ort21=Label(pn3,text=ortuc,font=("Bold",10)).place(x=190,y=320)
        ort22=Label(pn3,text="Ücret ortalaması",font=("Bold",10)).place(x=85,y=320)

        
        print(ortuc)

        #print(a,b)


        lstx.pack(padx=20,pady=30)




        
        pass
    pn3= Tk()
    pn3.title("öğrenci liste ekranı")
    pn3.geometry("500x500")
    var=IntVar()
        
    #ck.grid(row=0,column=2)
    #ck1= Checkbutton(pn3,text="Soyadına göre sıralama")    
    #ck1.grid(row=2,column=2)
    #ck2= Checkbutton(pn3,text="Numarasına göre sıralama")    
    #ck2.grid(row=4,column=2)

    frm=LabelFrame(pn3,text="Listelenmek istenen değerler",padx=50,pady=50)    
    frm.pack(padx=10,pady=10)

    btn12=Button(frm,text="LİSTELE",width=20,bg="gray",command=lst()).place(x=70,y=270)
    btn13=Button(frm,text="ÇIKIŞ",width=20,bg="yellow",command=pn3.destroy).place(x=220,y=270)
    #btn12.pack()
    #btn13.pack()
    #ck= Checkbutton(pn3,text="Öğrenci Adı",variable=var,height=3).place(x=80,y=300)
    
pn2=Tk()

pn2.title("ÖĞRENCİ İŞLERİ")
pn2.geometry("500x500")

btn11=Button(pn2,text="ÖĞRENCİ KAYDI",height=5,width=15,bg="red",command=ekrgrn).place(x=70,y=180)

btn21=Button(pn2,text="ÇIKIŞ",height=5,width=15,bg="blue",command=pn2.destroy).place(x=288,y=180)

btn31=Button(pn2,text="ÖĞRENCİ LİSTELE",height=5,width=15,bg="aqua",command=ekrlst).place(x=175,y=180)


