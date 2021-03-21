import requests

from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk




def sec():
    dstl=lkste.curselection()
          
    dst=lkste.get(dstl)
    #print(veri2)
    c=sz.get(dst,'yok olm')
                 
    #for e in veri2:
    #    mx= e.find('a',href=True)
        

    imdx='https://www.imdb.com' + c
    print(imdx)
    r1=requests.get(imdx)
    soup1=BeautifulSoup(r1.content,'html.parser')
    veri=soup1.find('table',attrs={'class':'cast_list'})
#print(veri)
    vr3=veri.find_all('td',attrs={'class':'primary_photo'})
    
    #
    #print(soup1)
    #veri1=soup1.find('div',attrs={'id':'filmography'})
    #print(veri1)   

    #vr2=veri1.find_all('a')
      
        
    z=[[]]
    cm=[] 
    for fx in vr3:
    #print(fx)
        vx=fx.find('img')
    
    #print(vx)
        fm1=vx['alt']
    
    
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
        #print(veri1)       
        vr2=veri1.find_all('b')
        #print(cm)      
        lstx3["columns"]= cm
    #print(lstx2["columns"])
        lstx3.column("#0",width = 2)
    #print(cm[i])
        
        for k in lstx3["columns"]:
            lstx3.column(k,width=85)
        
    
  

   
   # j=1
        print(i)       
        a=[]
        print(cm[i])
        a.append(cm[i])

        for fm in vr2:
        #print('4',fm.text)
             a.append(fm.text)
        z.append(a)
        i=i+1

    i=0
    ij=[]
    for ij in z:
    
        lstx3.insert('',"end",text='',values=(ij))
        i = i + 1 
    #rint(ij)
    
    


    
    lstx3.pack()    


        
    print(dst)
    


sz={}
imd='https://www.imdb.com/chart/top/'

r=requests.get(imd)

soup=BeautifulSoup(r.content,'html.parser')
cariekr=Tk()
cariekr.geometry("500x500")

    
lstx2=ttk.Treeview(cariekr,height="21")

ekr=Tk()
ekr.geometry("500x500")

    
lstx3=ttk.Treeview(ekr,height="21")


    
ttk.Style().theme_use("clam")    
ttk.Style().configure('Treeview',background='silver',foreground='green',fieldbackground="silver")
ttk.Style().map('Treeview',background=[('selected','green')])





flmler=[]
veri=soup.find('table',attrs={'class':'chart full-width'})
veri1=veri.find('tbody',attrs={'class':'lister-list'})
veri2=veri1.find_all('td',attrs={'class':'posterColumn'})
for i in veri2:


    ax= i.find('img')['alt']
    
    
    
    b=i.find('a',href=True)
    c=b['href']
    flmler.append(ax)
    sz[ax]=c
   # print(ax,c)

lkste=Listbox(cariekr,width= 95,height=35)
    
for i in flmler:
       
      
    lkste.insert(1,i)

lkste.pack(padx=10,pady=30)
btn8=Button(cariekr,text="bas bakalım",command=sec).place(x=180,y=450)







