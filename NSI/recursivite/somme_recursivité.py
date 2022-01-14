
"""
L=[2,12,1,8,5,10,20]

def sommeliste(liste = L):
    if len(liste) <= 1:
        print("la")
        return liste[0]
    else:
        print(liste[0])
        return liste[0]+sommeliste(liste[1:])
    
print(sommeliste())
"""
import random
import timeit

def initListe(n):
    l = [random.randint(0,100) for i in range(n)]
    return l

def sommeliste_Recursive(liste):
    if len(liste) <= 1:
        print("la")
        return liste[0]
    else:
        print(liste[0])
        return liste[0]+sommeliste_Recursive(liste[1:])
    
def sommeliste_iterative(liste):
    Somme = 0
    for i in liste:
        Somme += i
    return Somme


nb = int(input("saisir le nombre d'elements de la liste voulu : "))
L = initListe(nb)

debut = timer()
resulat = sommeliste_iterative(L)
fin = timer()

print("result iterative : ", resulat)
print("time : ", fin-debut)

debut = timer()
resulat = sommeliste_Recursive(L)
fin = timer()

print("result recursif : ", resulat)
print("time : ", fin-debut)