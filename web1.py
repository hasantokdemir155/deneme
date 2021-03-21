import requests

from bs4 import BeautifulSoup

imd='https://www.imdb.com/chart/top/'

r=requests.get(imd)

soup=BeautifulSoup(r.content,'html.parser')

veri=soup.find_all('table',{'class':'chart full-width'})

#print(veri[0])
  
#veri2= soup.find("table",attrs={'class':'chart full-width'})

ft=(veri[0].contents)[len(veri[0].contents)-2]

ft=ft.find_all('tr')

for fm in ft:
    filmbs= fm.find_all("td",{"class":"titleColumn"})
    print(filmbs[0].text)
    
#print(ft)
