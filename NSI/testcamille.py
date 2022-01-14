from math import e, exp
def racine():
    x=0
    y = -1
    while y<0:
        x=x+0.1
        y=exp(x)-(x+2)
    return x-0.1,x

print(racine())
L =[4,"A","B","C","D",None]
print(type(L))
i = 2
for k in range(L[0]+1, i,-1):
    L[k] = L[k-1]
    print(k)
E= 5
L[i] =E
L[0]+=1
print(L)

L[5] = 15

print(L)



K = [None for i in range(10)]
print(K)


print(len(L))


print(L.index(15))