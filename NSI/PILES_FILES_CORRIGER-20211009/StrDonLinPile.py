# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 15:40:39 2020

@author: mfb
"""

def Creer_Pile_Vide(n):
    Pile = []
    Pile.clear()                               # Création de la pile sans éléments
    [Pile.append(None) for i in range(n+1)]   # Initialisation de la pile avec les n éléments à "None"
    Pile[0] = 1                                # Initialisation de la pile comme étant vide : 
                                               # L'élément d'index 0 contient le prochain index où il faudra stocker la donnée.
    return(Pile)

def Creer_Pile_VideBis(n):
    Pile=[None] * (n+1)                        # Création et Initialisation de la pile avec les n éléments à "None"
    Pile[0] = 1                                # Initialisation de la pile comme étant vide : 
                                            # L'élément d'index 0 contient le prochain index où il faudra stocker la donnée.
    return(Pile)


def Empiler(Pile,Val):
    if( ( (Pile[0] < 1) or (Pile[0] == len(Pile))) ):
        print("La pile est pleine ou mal définie !")
        return(False)
    else:
        Pile[Pile[0]] = Val
        Pile[0] = Pile[0] + 1
        return(True)

def Depiler(Pile):
    if( (Pile[0] <= 1) ):
        print("La pile est vide ou mal définie !")
        return(False)
    else:
        Pile[0] = Pile[0] - 1
        Val = Pile[Pile[0]]
        return(Val)
        

#P = Creer_Pile_VideBis(6)
P = Creer_Pile_Vide(6)
print(P)
Empiler(P,3)
Empiler(P,7)
Empiler(P,1)
Empiler(P,8)
print(P)
print(Depiler(P))
print(P)