

isim=[]

def hrf(isim):
    
    s=0
    for n in isim:

        print(n[s])
        s= s + 1

for i in range(0,3):

        n=input('isim gir')        
        isim.append(n)
print(isim)

hrf(isim)
