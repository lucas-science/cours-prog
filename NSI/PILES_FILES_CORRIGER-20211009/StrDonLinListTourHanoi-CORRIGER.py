# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 23:15:08 2020

@author: mfb
"""
# Tour de Hanoï

# Création d'une pile sans taille définie
def CreaStack():
    P = []                                # Création de la Pile en mémoire  
    return(P)
    
# Empilage par la méthode '.append()', sans contrôle de taille de pile
def Empiler(Pile,Val):
    Pile.append(Val)

def PileVide(Pile):
    return(Pile == [])
        
def Depiler(Pile):
    return(Pile.pop())

#                 Pile 1 Pile 3  Pile 2
def TourDeHanoi(n,depart,arrivee,inter):
    global cmpt
    if(n != 0):
        TourDeHanoi(n-1,depart,inter,arrivee)
        Empiler(arrivee,Depiler(depart))
        TourDeHanoi(n-1,inter,arrivee,depart)
        cmpt = cmpt +1
    return


# Création des 3 piles vides
P1 = CreaStack()
P2 = CreaStack()
P3 = CreaStack()

NbDisques = int(input("Saisir le nombre de disques de la tour de départ : "))

# Initialisation de la pile de départ P1, soit le nombre de disques au départ
for i in range(NbDisques,0,-1):
    Empiler(P1,i)
cmpt = 0
print(P1,P2,P3)

TourDeHanoi(NbDisques,P1,P3,P2)
print(P1,P2,P3)
print(cmpt)
