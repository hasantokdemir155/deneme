import requests
import pandas as pd
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk


cariekr=Tk()
cariekr.geometry("500x500")

lstx2=ttk.Treeview(cariekr,height="21")
    
ttk.Style().theme_use("clam")    
ttk.Style().configure('Treeview',background='silver',foreground='green',fieldbackground="silver")
ttk.Style().map('Treeview',background=[('selected','green')])





imd='https://www.imdb.com/title/tt1392190/'

r=requests.get(imd)

soup=BeautifulSoup(r.content,'html.parser')

veri=soup.find('table',attrs={'class':'cast_list'})
#print(veri)
vr3=veri.find_all('td',attrs={'class':'primary_photo'})
print(vr3)




a=[]
z=[[]]
cm=[] 

for fx in vr3:
    #print(fx)
    vx=fx.find('img')
    
    #print(vx)
    fm1=vx['alt']
    print(fm1)
    cm.append(fm1)
i=0
for y in vr3 :
    b=y.find('a',href=True)
    
    c=b['href']
    #print(c)
    imdx='https://www.imdb.com' + c
    print(imdx)
    r1=requests.get(imdx)
    soup1=BeautifulSoup(r1.content,'html.parser')
    
    veri1=soup1.find('div',attrs={'id':'filmography'})
       
    vr2=veri1.find_all('b')
      
    lstx2["columns"]= cm
    #print(lstx2["columns"])
    lstx2.column("#0",width = 2)
    
    #print(cm[i])

    for k in lstx2["columns"]:
        lstx2.column(k,width=85)
        

   # for k in lstx2["columns"]:
   #     lstx2.heading(k,text=k)   
    


   
   # j=1
    a=[]
    print(i)
    a.append(cm[i])
    for fm in vr2:
        #print('4',fm.text)
        a.append(fm.text)
        
    z.append(a)
    print(a[0])
    input()
    i= i + 1
ij=[]
i=0


for ij in z:
    
    lstx2.insert('',"end",text='',values=(ij))
    i = i + 1 
    #rint(ij)
    
    


    
lstx2.pack()    

