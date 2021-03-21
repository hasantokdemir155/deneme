import json
import pymongo

#json dosyalardaki verileri alıp mongo db üzrine kaydetme hareketleri üzerine bir çalışma



with open('den4.json','r') as dsy:
     oku=json.load(dsy)



myc=pymongo.MongoClient("mongodb://localhost:27017")

mydb=myc["deneme"]
mycll= mydb["isimler"]

if isinstance(oku, list): 
    mycll.insert_many(oku)   
else: 
    mycll.insert_one(oku) 



print(oku)

halt

