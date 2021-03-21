import sqlite3



bgln1=sqlite3.connect("okul.db")
kmt1=bgln1.cursor()
kmt1.execute("select * from ogrnci,snflar where ogrnci.ogno=snflar.oggno group by snf")
                     #where ognot > 50 order by ogfyat asc"  )
    
kaytlar=kmt1.fetchall()
i=0
for  i in kaytlar:

    print(i[0],i[1],i[2],i[3],i[6])
    
