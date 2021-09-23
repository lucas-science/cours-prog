# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 10:17:20 2020

@author: mfb
"""

# Changement de base : binaire, octal vers décimal
def bTodec(mot,b):
    assert (b>1 and b<17) ,"b doit être compris entre 2 et 16"
    assert (type(mot) == str), "Le nombre n doit être une chaîne de caractères"
    signes=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    result=0
    p=len(mot)
    for i in range(p):
        result = result + signes.index(mot[i])*b**(p-i-1)
    return result

def bTodecRecursif(mot,b,signes):
    result=0
    p=len(mot)
    if(p <= 1):
        return(signes.index(mot[0]))
    else:
        result =  signes.index(mot[0])*b**(p-1) + bTodecRecursif(mot[1:],b,signes)
        return (result)

def bTodecRecursifPedagogique(mot,b,signes):
    result=0
    p=len(mot)
    if(p <= 1):
        print("Nombre trivial = ",mot)
        return(signes.index(mot[0]))
    else:
        print("Nombre à traiter = ",mot)
        result = signes.index(mot[0])*b**(p-1)
        print("Valeur poid binaire empilé = ",result)
        result =  result + bTodecRecursifPedagogique(mot[1:],b,signes)
        print("Dépilage : somme de poids binaires = ",result)
        return (result)

b = int(input("Saisir la base d'origine : "))
mot = str(input("Saisir la chaine de caractères représentant le nombre : "))

# Ces instructions ne doivent pas être mises dans une fonction récursive car consomme beaucoup de mémoire
assert (b>1 and b<17) ,"b doit être compris entre 2 et 16"
assert (type(mot) == str), "Le nombre n doit être une chaîne de caractères"
signes=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]


print("Résultat itératif : ",bTodec(mot,b))
print("Résultat récursif : ",bTodecRecursifPedagogique(mot,b,signes))
