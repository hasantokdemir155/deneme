import pymongo
import pandas as pd
import json








myc=pymongo.MongoClient("mongodb://localhost:27017")

mydb=myc["deneme"]
mycll= mydb["isimler"]


print(myc.list_database_names())
print(mydb.list_collection_names())

myq = {'label': 'Site:'}
soncx=mycll.find(myq)


for i in soncx:
    input()
    print(i)





#sonc=mycll.find()
s=[]
sonc=mycll.find({},{"_id":0,"fields":1})
k=0

for i in sonc:
    #print(i['_id'])
    s.append(i)
    k= k +1 
    print(k)

for m in range(0,4):
    
    print(s[12]['fields'][m]['label'])



#sonc1=mycll.find({},{"_id":0}).sort("adres",1)


#sonc1=mycll.find({},{"_id":0,"type":1,"topping":1})

#for i in sonc1:
#    print(i)
#pcount=mycll.count_documents({})    


#print(dt['errors'])

#v=dt['errors']

#for i in v:
#    print(i['code'],i['source'],i['title'])






