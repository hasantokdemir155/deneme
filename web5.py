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





imd='https://www.kariyer.net/is-ilanlari/#&so=rdFilterAramaSecenekleri1'

r=requests.get(imd)

soup=BeautifulSoup(r.content,'html.parser')
veri=soup.find('body',attrs={'class':'header-static'})
vr3=veri.find('main',attrs={'class':'sub-wrapper'})
ver4=vr3.find('div',attrs={'class':'two-cols'})
ver5=ver4.find('div',attrs={'class':'right-col'})
ver6=ver5.find('div',attrs={'class':'subpage-container'})
ver7=ver6.find('div',attrs={'class':'is-ara-wrapper'})
ver8=ver7.find('div',attrs={'id':'divList'}).text
#ver9=ver8.find_all('div')
#ver10=ver9.find_all('a')
print(ver8)




#vr3=veri.find_all('td',attrs={'class':'primary_photo'})





lstx2.pack()    

