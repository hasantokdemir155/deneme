
snf=[]
ognt=[]
ogru=[]
class okul:

    def __init__ (self,ogno=5,ogad="ali",ogsoyad="tok",ognot=0,ogrucr=0):
        
        self.ogno= ogno
        self.ogad= ogad
        self.ogsoyad= ogsoyad
        self.ognot = ognot
        self.ogrucr=ogrucr
        
    def notata(self):    
        self.ognot = (self.ognot+45)
        return self.ognot
    
    def ogrucrtata(self):
        self.ogrucr= (self.ogrucr*1.05)
    
ogr1 = okul()

#ogr1.notata

for i in range(0,5):
    
    ogr1.ogno=input()
    ogr1.ognot=int(input("öğrenci notu"))
    ogr1.ogrucr= int(input("öğrenim ücreti"))

    snf.append(ogr1.ogno)
                     
    ogr1.notata()    
    ognt.append(ogr1.ognot)

    ogr1.ogrucrtata()
    ogru.append(ogr1.ogrucr)
#ogr1.ogno = self.ogno

print(snf,ognt,ogru)

