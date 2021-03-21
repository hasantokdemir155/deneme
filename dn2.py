
def islm(x,y):
    return x*((x+y)/2)


sy=[]
sy1=[]

for i in range(0,4):
    sy.append(input())
    sy1.append(input())

print(sy,sy1)
#print(sy[2])
mp1 = map(lambda x,y:x*((x+y)/2),sy,sy1)

#mp1 = map(lambda ,sy,sy1)

print(list(mp1))
