# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 10:22:45 2020

@author: mfb
"""

def CreaStack():
    Pile = []
    Pile.append(1)
#    Pile[0]
    return(Pile)

def CreaStackBis():
    Pile = []
#    Pile[0]
    return(Pile)
    

def Empiler(P,Val):
    if ( (P[0] > 0) ):                      # La pile n'est ni pleine ni mal définie ?
        P.append(Val)                       # La méthode .append() sans paramètre -> dépile l'élément au sommet de la pile
        P[0] = P[0] + 1
        return(True)
    else:
        print("La pile est pleine ou mal définie !")
        return(False)        

def EmpilerBis(P,Val):                      # Aucun contrôle sur la pile
        P.append(Val)                       # La méthode .append() sans paramètre -> dépile l'élément au sommet de la pile

    
def Vide(P):
    if(len(P) > 0):                         # retourne la valeur True si la pile est vide, False autrement
        return (True)
    else:
        return (False)
    
def VideBis(P):
        return (P == [])                    # retourne la valeur True si la pile est vide, False autrement


def Depiler(P):
    if ( (P[0] > 1) ):                      # La pile est-elle vide ?
        Val = P.pop()                       # La méthode .pop() sans paramètre -> dépile l'élément du sommet de la pile
        P[0] = P[0] - 1                     # 
        return(Val)
    else:
        print("La pile est vide !")
        return(False)        

def DepilerBis(P):                          # Si la pile est vide, la ligne de code suivante est exécutée, sinon la chîne de caractères "La pile est vide !" est affichée, puis sort de la fonction.
    assert not VideBis(P), "La pile est vide !" 
    return(P.pop())



P = CreaStack()
print(P)
Empiler(P,3)
Empiler(P,7)
Empiler(P,1)
Empiler(P,8)
print(P)
print(Depiler(P))
print(Depiler(P))
print(Depiler(P))
print(Depiler(P))
print(Depiler(P))
print(P)

P = CreaStackBis()
print(P)
EmpilerBis(P,3)
EmpilerBis(P,7)
EmpilerBis(P,1)
EmpilerBis(P,8)
print(P)
print(DepilerBis(P))
print(DepilerBis(P))
print(DepilerBis(P))
print(DepilerBis(P))
print(DepilerBis(P))
print(P)