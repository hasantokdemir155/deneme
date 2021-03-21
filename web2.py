import requests

from bs4 import BeautifulSoup

imd='https://www.imdb.com/title/tt1392190/'

r=requests.get(imd)

soup=BeautifulSoup(r.content,'html.parser')

veri=soup.find('table',attrs={'class':'cast_list'})
#veri1=veri.find('a')
#print(veri[0])
#print(veri)
#veri2= soup.find("table",attrs={'class':'cast_list'}).select('tr:nth-of-type(2)> td')
#print(veri2)

#ver1=veri.find_all('tr',attrs={'class':'odd','class':'even'})
vr3=veri.find_all('td',attrs={'class':'primary_photo'})
print(vr3)
#print(vr3['href'])
#vmx=vr3.find_all('img')
for fx in vr3:
    #print(fx)
    print(fx)
    vx=fx.find('img')
    #print(vx)
    print(vx['alt'])

#print(vmx)
vr2=veri.select('a')
#vrx=veri.a.get('href').veri.a.get('title')

#print(vr3)

#print(vr2)
#print(ver1)
#print(veri)
#ft=(veri[0].contents)[len(veri[0].contents)-2]
#ft=veri2. find_all('tr')


#print(veri2)
i=1
cm=[]
for fm in vr2:
    #print(fm.a.get('href'),fm.a.get('title'))   
    cm.append(fm.text)
    
    #print(cm)
for c in cm:
    
    print(cm[i])
    i=i+3

    
#print(ft)
