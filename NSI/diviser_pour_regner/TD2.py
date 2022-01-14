from timeit import default_timer as timer
<<<<<<< HEAD
L=[95, 28, 36, 52, 85, 56, 34, 59, 17, 26, 16, 25, 69, 98, 4, 85, 81, 48, 11, 57]
=======
from random import randint
N = int(input("Taile de la liste : "))
L = [randint(1,100) for i in range(N)]
>>>>>>> 47c9202d99e37f37b519f00940011b715c19af0a

cpmt = 0

def cherche_max_recurs(l):
    global cpmt
    cpmt += 1
    if len(l) == 1:
        return l[0]
    else:
        return max(l[0],cherche_max_recurs(l[1:]))

cpmt2 = 0
def cherche_max_iter(l):
    global cpmt2
    max = 0
    for i in l:
        cpmt2 += 1
        if max < i:
            max = i
    return max

def getMax(a,b):
    if a > b:
        return a
    else:
        return b
cpmt3 = 0
def cherche_max_recurs_divise(l,d,f):
    global cpmt3
    cpmt3 += 1
    global cpmt_recurs
    if d == f:
        return l[d]
    m = (d+f)//2
    return (getMax(cherche_max_recurs_divise(l,d,m),cherche_max_recurs_divise(l,m+1,f)))


#print(cherche_max_recurs_divise(L,0,len(L)-1))




print("----------Recurs----------")
debut1 = timer()
print(cherche_max_recurs(L))
fin1 = timer()
print(f"Timer : {fin1-debut1}\nNombre d'appel : {cpmt}")

print("----------Iterative----------")

debut2 = timer()
print(cherche_max_iter(L))
fin2 = timer()
print(f"Timer : {fin2-debut2}\nNombre d'appel : {cpmt2}")

print("----------Recurs divise pour raigné ----------")

debut3 = timer()
print(cherche_max_recurs_divise(L,0,len(L)-1))
fin3 = timer()
print(f"Timer : {fin3-debut3}\nNombre d'appel : {cpmt3}")
