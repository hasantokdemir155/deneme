from tkinter import *
from tkinter import ttk
from sklearn.datasets import fetch_20newsgroups
import requests
import pandas as pd
from bs4 import BeautifulSoup


#data= fetch_20newsgroups

#print(fetch_20newsgroups.feature_names)
imd='https://www.trendyol.com/sr?q=tutku+erkek+atlet&qt=tutku+erkek+atlet&st=tutku+erkek+atlet&os=1&pi=6'

r=requests.get(imd)

soup=BeautifulSoup(r.content,'html.parser')

veri=soup.find('script',attrs={'type':'application/javascript'})

veri1=veri.find('window.__SEARCH_APP_INITIAL_STATE__ ')
print(veri1)
