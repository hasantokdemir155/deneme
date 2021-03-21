import pymongo
import pandas as pd
import json



#with open('den3.json') as f:
 #   dt=json.load(f)
with open('den3.json') as f:
    dt=json.load(f)
print(dt['jsonapi'])
print(dt['errors'][0])
print(dt['errors'][1]['source'])

with open('den5.json') as f:
    dt=json.load(f)


#v=dt['article']
v=dt
print(dt['article'][0]['id'])
print(dt['article'][1]['id'])
print(dt['blog'][0]['name'])


for i in v:
    print(i[2])
print(dt['article'][0])
input()
print(dt['blog'][0])
    #for m in i:
##        print(m)
    # print(i)
   # print(i['id'],i['language'],i['edition'],i['author'])






#myc=pymongo.MongoClient("mongodb://localhost:27017")

#mydb=myc["deneme1"]
#mycll= mydb["isimler2"]


#sonc=mycll.find_one()

#sonc=mycll.find({},{"_id":0,"ad":1,"ad3":1,"ad4":1})

#sonc1=mycll.find({},{"_id":0}).sort("adres",1)


#sonc1=mycll.find({},{"_id":0,"type":1,"topping":1})

#for i in sonc1:
#    print(i)
#pcount=mycll.count_documents({})    


#print(dt['errors'])

#v=dt['errors']

#for i in v:
#    print(i['code'],i['source'],i['title'])






