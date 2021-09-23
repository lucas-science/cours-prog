# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 18:00:13 2020

@author: mfb
"""

def DecToBase(n,b):
    assert (b==2 or b == 8 or b== 16) , " Uniquement avec une des bases usuelles "
    symboles = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    res = ""
    while (n!=0):
        res = symboles[n%b] + res
        n = n//b
    return res


def DecToBaseRecursif(n,b,symboles):
    if( n < b ):
       return(symboles[n%b])
    else:
        return( DecToBaseRecursif(n//b,b,symboles) + symboles[n%b] )

def DecToBaseRecurDidactique(n,b,symboles):
    res = ""                                                    # Uniquement pour afficher et comprendre le fonctionnement
    if( n < b ):
       res = (symboles[n%b])
       print("dernier appel, reste = ",res)                     # Uniquement pour afficher et comprendre le fonctionnement
       return(res)
    else:
        print("n = ",n,end=" ")                                 # Uniquement pour afficher et comprendre le fonctionnement
        reste = symboles[n%b]
        print("reste = ",reste)                                 # Uniquement pour afficher et comprendre le fonctionnement
        res = DecToBaseRecurDidactique(n//b,b,symboles) + reste
        print("res = ",end="")                                  # Uniquement pour afficher et comprendre le fonctionnement
        print(res)                                              # Uniquement pour afficher et comprendre le fonctionnement
        return( res )

Nb = int(input("saisir le nombre décimale à convertir: "))
Base = int(input("saisir base de conversion : "))

print("Le nombre converti est (itératif) : ", DecToBase(Nb,Base))
# Ces instructions ne doivent pas être mises dans une fonction récursive car consomme beaucoup de mémoire
assert (Base==2 or Base == 8 or Base== 16) , " Uniquement avec une des bases usuelles "
symboles = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
print("Le nombre converti est (récursif) : ", DecToBaseRecurDidactique(Nb,Base,symboles))



print("here", 27%16)
print("here", 28%2)