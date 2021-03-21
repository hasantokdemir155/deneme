from tkinter import *
from tkinter import ttk
import sqlite3
import matplotlib.pyplot as pyp

class calsma:
    
    def __init__(self,ono,matnot,fennot,sosnot,ort):
        self.ono= ono
        self.matnot=matnot
        self.sosnot=sosnot
        self.fennot=fennot
        self.ort=ort
    def ort1(self):    
        self.ort = (self.matnot+self.sosnot+self.fennot)/3
      #  return ort1

    

def graf():
    yıllar=[]
    sayılar=[]
    for i in kaytlar:

        yıllar.append(i[0])
        sayılar.append(i[3])
                    
        
    #yıllar=[2001,2002,2003,2004,2005,2006,2007]
    #sayılar=[12,14,15,16,17,18,19]
    pyp.plot(yıllar,sayılar)
    pyp.show()
def graf1():
    yıllar=[]
    sayılar=[]
    for i in kaytlar:

        yıllar.append(i[0])
        sayılar.append(i[4])
                    
    
    #yıllar=[2001,2002,2003,2004,2005,2006,2007]
    #sayılar=[12,14,15,16,17,18,19]
    pyp.plot(yıllar,sayılar)
    pyp.show()




#ogrno=input('ogrenci no')
#matnot1=input('matnot not')
#fennot1=input('turnot not')
#sosnot1=input('sosnot not')






sc=Tk()
sc.geometry("500x500")

mytab=ttk.Notebook(sc)
mytab.pack(pady=15)
mytab1= ttk.Frame(mytab,width=400,height=400)
mytab2= ttk.Frame(mytab,width=400,height=300)
mytab.add(mytab1,text="ilk tab")
mytab.add(mytab2,text="2.tab")


#button1=Button(mytab1,text="çalışıyoz ulan").pack()

bgln1=sqlite3.connect("okul.db")
kmt1=bgln1.cursor()
        #var=intVar()
        
        #ogno,ogad,osoyad,ogfyat,ognot
kmt1.execute("select * from ogrnci order by ogno asc")
                     #where ognot > 50 order by ogfyat asc"  )
kaytlar=kmt1.fetchall()
lstx=ttk.Treeview(mytab1,height="14")

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
for i in kaytlar:
    
        a=i[0]
        b=i[1]
        c=i[2]
        d=str(i[3])
        e=str(i[4])
        #tp= tp + int(e)
        #tpuc=tpuc+ int(d)
        #s = s + 1
        lstx.insert('',"end",text="",values=(a,b,c,d,e))

lstx.pack(padx=20,pady=30)

bgln2=sqlite3.connect("okul.db")
kmt2=bgln2.cursor()
kmt2.execute("select * from snavlar")
                     #where ognot > 50 order by ogfyat asc"  )
kaytlar1=kmt2.fetchall()
lstx1=ttk.Treeview(mytab2,height="10")

lstx1["columns"]= ("ognoa","turkcenot","matmanot","fennot","sosnot","ort")

lstx1.column("#0",width = 2)

lstx1.column("ognoa",width=40)
lstx1.column("turkcenot",width=60)
lstx1.column("matmanot",width=60)
lstx1.column("fennot",width=60)
lstx1.column("sosnot",width=70)
lstx1.column("ort",width=61)
        
        
lstx1.heading("ognoa",text="Öğrencino")
lstx1.heading("turkcenot",text="Türkçe")
lstx1.heading("matmanot",text="Matematik")
lstx1.heading("fennot",text="Fen Bilgisi")
lstx1.heading("sosnot",text="Sosyal")
lstx1.heading("ort",text="Ortalama")
ort=1
for i in kaytlar1:
    
        a=i[0]
        b=i[1]
        c=i[2]
        d=str(i[3])
        e=str(i[4])
        sen=calsma(a,b,c,int(d),ort)
        sen.ort1()
        f=sen.ort
        f=round(f,2)
        print(f)
        #tp= tp + int(e)
        #tpuc=tpuc+ int(d)
        #s = s + 1
        lstx1.insert('',"end",text="",values=(a,b,c,d,e,f))

lstx1.pack(padx=1,pady=20)

button1=Button(sc,text="Öğrenci ücret grafiği",command=graf).pack()
button2=Button(sc,text="Öğrenci not grafiği",command=graf1).pack()


sc.mainloop()
