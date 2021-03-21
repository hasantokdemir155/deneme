import PyQt5


import pandas as pd

s=[]

with open('audiology.txt','r+') as f:
    for i in range (1,5):
       s=f.readline()
       s=s.replace('[','')
       s=s.replace(']','')     
       
       s=s.split(',')
       
       print(s[7]) 
      # print(s)
       #for y in s:
        #   print(y)
        
       


#orn=pd.read_txt('audiology.txt')
#veri=pd.DataFrame(orn)
#print(veri)



#print(ornek1['adlar'],mc)
#print(ornek2['esya'])
