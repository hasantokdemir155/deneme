import pymongo

myc=pymongo.MongoClient("mongodb://localhost:27017")

mydb=myc["deneme"]
mycll= mydb["isimler"]


sonc=mycll.find_one()

#sonc=mycll.find({},{"_id":0,"ad":1,"ad3":1,"ad4":1})

#sonc1=mycll.find({},{"_id":0}).sort("adres",1)


sonc1=mycll.find({},{"_id":0,"type":1,"topping":1})

for i in sonc1:
    print(i)
pcount=mycll.count_documents({})    


print(pcount)
