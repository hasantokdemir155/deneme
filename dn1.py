from functools import  reduce
from tkinter import *

def klhsp(x,y):
    return x*((x+y)/2)




#sy=[3,5,7]
#sy1=[9,11,13]

#rd2=reduce(klhsp,sy1)
#rd1=reduce(klhsp,sy)
#print(rd1,rd2)

#map1= map(klhsp,sy,sy1)

#print(list(map1))

pn1=Tk()
pn1.geometry("500x400")

yaz=Label(pn1,text='İSİM')
yaz.grid(row=0,column=6)

#ismgr= Entry(pn1,width="12")
#ismgr.grid(row=3,column=0)

tkla= Button(pn1,text ="buton1")
tkla.pack(padx=30,pady=45)

mainloop

