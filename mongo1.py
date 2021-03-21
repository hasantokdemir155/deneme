import pymongo

myc=pymongo.MongoClient("mongodb://localhost:27017")

mydb=myc["deneme"]
mycll= mydb["isimler"]


prdc={"ad":"hasan","soyad":"vel"}


print(myc.list_database_names())

#sonc=mycll.insert_one(prdc)

#print(sonc)
#print(sonc.inserted_id)

prdclist=[{"ad":"hasan","soyad":"vel"},
          {"ad":"hasan","soyad":"vel"},
          {"ad3":"hasan","soyad":"vel","adres":"tokat"},
          {"ad4":"hasan","soyad":"vel","maas":2500}
            

    ]

sonc= mycll.insert_many(prdclist)
