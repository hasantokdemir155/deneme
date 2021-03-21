import sqlite3


bgln=sqlite3.connect("okul.db")
kmt=bgln.cursor()
i= 6

def vertaban() :
    
    kmt.execute("create table if not exists ogrnci(ogno integer,ogad text,osoyad text,ogfyat integer,ognot integer)")
    bgln.commit()

def vergrs():
    ogno=input("öğrenci no")
    ogad=input("öğrenci ad")
    osoyad=input("öğrenci soyad")
    ogfyat=input("öğrenci ücreti")
    ognot=input("öğrenci notu")
    kmt.execute("insert into ogrnci values(@p1,@p2,@p3,@p4,@p5)",(ogno,ogad,osoyad,ogfyat,ognot))  
    bgln.commit()
    bgln.close


while i > 5 :
       
    vertaban()
    vergrs()

    i=int(input("i sayısını gir"))
    
