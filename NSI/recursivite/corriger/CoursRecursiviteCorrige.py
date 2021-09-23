# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 17:33:16 2020

@author: mfb
"""
from random import randint
from timeit import default_timer as timer

L= [0,1,2,3,4,5,6,7,8,9]
print(L[0:])

def InitListe(n):
    L = [randint(0,100) for i in range(n)]
    return (L)

def SommeListe(Liste):
    somme = 0
    for i in range(len(Liste)):
        somme = somme + Liste[i]
    return(somme)
    
def SommeListeRecursive(L):
    if(len(L) <= 1):
        return(L[0])
    else:
        return(L[0]+ SommeListeRecursive(L[1:]))

def SommeListeRecursivePedagogique(L):
    print(L)                                            # Uniquement pour afficher et comprendre le fonctionnement
    if(len(L) <= 1):
        print("Val end= ", L[0])
        return(L[0])
    else:
        somme = L[0]+ SommeListeRecursivePedagogique(L[1:])
        print("Dépilage et calcul somme : ",somme)      # Uniquement pour afficher et comprendre le fonctionnement
        return(somme)

def Mini(a,b):
    c = b
    if(a < b ):
        c = a
    return(c)
    
def MinimumIterative(Liste):
    mini = Liste[0]
    for i in range(1,len(Liste),+1):
        mini = Mini(mini,Liste[i])
    return(mini)
        
def MinimumRecursive(L):
    if(len(L) <= 1):
       return(L[0])
    else:
        return(Mini(L[0],MinimumRecursive(L[1:])))

def MinimumRecursivePedagogique(L):
    print(L)                                            # Uniquement pour afficher et comprendre le fonctionnement
    if(len(L) <= 1):
       print("Val end= ", L[0])                         # Uniquement pour afficher et comprendre le fonctionnement
       return(L[0])
    else:
        val = Mini(L[0],MinimumRecursivePedagogique(L[1:]))
        print("Dépilage et recherche Val min= ", val)   # Uniquement pour afficher et comprendre le fonctionnement
        return(val)
        
def PuissanceN(val,exposant):
    if(exposant <= 1):
        return(val)
    else:
        return(val * PuissanceN(val,exposant-1))

def PuissanceNPedagogique(val,exposant):
    print("Exposant = ",exposant)                       # Uniquement pour afficher et comprendre le fonctionnement
    if(exposant <= 1):
        print("exposant end = ",exposant)               # Uniquement pour afficher et comprendre le fonctionnement
        return(val)
    else:
        res = val * PuissanceNPedagogique(val,exposant-1)
        print("Dépilage et calcul puissance : ",res)    # Uniquement pour afficher et comprendre le fonctionnement
        return(res)

Nb = int(input("saisir le nombre d'éléments de la liste : "))
L = InitListe(Nb)

print("")
print("          Somme des éléments de la liste itérative")
print("")
debut = timer()
Resultat = SommeListe(L)
fin = timer()

print("contenu de la liste : ", L)
print("la somme des éléments de la liste vaut : ", Resultat)
print("temps exécution par itération (µs): ",fin-debut )

print("")
print("          Somme des éléments de la liste par récursivité")
print("")
debut = timer()
ResultatRecursif = SommeListeRecursivePedagogique(L)
fin = timer()

print("temps exécution par récursivité (µs): ",fin-debut)
print("la somme des éléments de la liste par récursivité vaut : ", ResultatRecursif)
print("")
print("          Recherche du minimum de la liste")
print("")
print("La valeur minimum itérative est : ",MinimumIterative(L))
print("La valeur minimum récursive est : ",MinimumRecursivePedagogique(L))


print("")
print("          Calcul de la puissance d'un nombre")
print("")
Nb = int(input("saisir la valeur du nombre à calculer : "))
exp = int(input("saisir la valeur de l'exposant : "))
print("Résultat calcul puissance = ", PuissanceNPedagogique(Nb,exp))
