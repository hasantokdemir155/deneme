import requests
import pandas as pd
import json




#print(sonc.text)[]


sonc=pd.read_json('dn.json')
sonc1=sonc

ds=open('dn.json','r')







soncx=sonc1['id']
print(sonc1['batters'][0]['batter'][3]['type'])
print(sonc1['topping'][0][0]['id'])
print(sonc1['id'])
print(sonc1['batters'][2]['batter'][1])
print(sonc1['topping'][2][2]['type'])
snc=sonc1['batters']
print(type(snc))
    
for i in range(0,3):
    print(sonc1['batters'][i])
    


#sn=json.loads(snc)
#print(snc)

#for i in sn:
    

 #   print(i)
#print(soncx)

#print(soncx['batter'])#soncx['batter'])

#for i in sonc1:
#    print(i)
