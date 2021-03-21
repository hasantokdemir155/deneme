import requests

from bs4 import BeautifulSoup

imd='https://www.imdb.com/name/nm0362766/'
#?ref_=nv_sr_srsg_3'

r=requests.get(imd)

soup=BeautifulSoup(r.content,'html.parser')

veri=soup.find('div',attrs={'id':'filmography'})
#veri1=veri.find('a')
print(veri)
 
#veri2= soup.find("table",attrs={'class':'cast_list'}).select('tr:nth-of-type(2)> td')
#print(veri2)

#ver1=veri.find_all('tr',attrs={'class':'odd','class':'even'})
#vr3=veri.find_all('b')
#print(vr3['href'])
vr2=veri.find_all('b')
print()
#print(vr3)

#print(vr2)
#print(ver1)
#print(veri)
#ft=(veri[0].contents)[len(veri[0].contents)-2]
#ft=veri2. find_all('tr')


#print(veri2)
i=1
#cm=[]
for fm in vr2:
   
 #   cm.append(fm.text)
    
    print(i,fm.text)
    i= i + 1
#for c in cm:
    
 #   print(cm[i])
  #  i=i+3

    
#print(ft)
