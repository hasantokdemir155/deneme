
import json

import pandas as pd


lnk='https://github.com/hadley/r4ds/blob/master/issues.json'
vrm=pd.read_json(lnk)


vr=pd.read_json('den2.json')

vr1=vr
vrx=vr1['owner']

#for i in range (0,20):

    #print(vrx[i]['login'],vrx[i]['id'],vrx[i]['url'])

print(vr1['forks'],vr1['id'])


#print(vr[0])




#s=[]

#with open('audiology.txt','r+') as f:
#    for i in range (1,5):
#       s=f.readline()
#       s=s.replace('[','')
#       s=s.replace(']','')     
       
      # s=s.split(',')
       
      # print(s[7]) 
      # print(s)
       #for y in s:
        #   print(y)
        
       


#orn=pd.read_txt('audiology.txt')
#veri=pd.DataFrame(orn)
#print(veri)



#print(ornek1['adlar'],mc)
#print(ornek2['esya'])
