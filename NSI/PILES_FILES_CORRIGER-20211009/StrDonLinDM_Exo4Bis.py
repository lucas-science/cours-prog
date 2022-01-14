# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 15:52:43 2020

@author: mfb
"""
Expression = []                             # Chaîne de caractères contenant l'expression mathématique

# Création d'une pile sans taille définie
def CreaStackBis():
    P = []                                # Création de la Pile en mémoire  
    return(P)
    
# Empilage par la méthode '.append()', sans contrôle de taille de pile
def EmpilerBis(Pile,Val):
    Pile.append(Val)

def PileVideBis(Pile):
    return(Pile == [])
        
def DepilerBis(Pile):
    Val = None
    if( PileVideBis(Pile) != True ):
        Val = Pile.pop()                    # Copie l'élément à dépiler dans une variable locale
    return(Val)                             # Retourne la valeur copiée ou la valeur None si pile vide.

def VerificationParBis(Expression):
    P = CreaStackBis()
    for i in range (0,len(Expression), 1):
        if(Expression[i] == "(" ):
            EmpilerBis(P,"o")
        elif(Expression[i] == ")" ):
            if( len(P) <= 0 ):              # Si la pile est vide après la détéction de ")", c'est que l'expression est déjà incohérente.
                print(P)
                return(False)
            else:
                DepilerBis(P)                
        print(P)
    return(P == [])

Math = input("Saisir l'expression mathématique à vérifier : ")

if(VerificationParBis(Math) == True):
    print("L'expression mathématique semble cohérente !")
else:
    print("L'expression mathématique est incohérente !")
