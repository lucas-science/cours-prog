# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 15:52:43 2020

@author: mfb
"""
Expression = []                             # Chaîne de caractères contenant l'expression mathématique

# création d'une pile à 'n' éléments
def CreaStack(n):
    Pil = []                                # Création de la Pile en mémoire  
    Pil.clear()
    [Pil.append(None) for i in range(n+1)]  # Initialisation de la pile à n éléments + l'index courant d'empilement
    Pil[0] = 1                              # Initialisation de l'index courant à la valeur d'index 1 -> Pile vide
    return(Pil)
    
def Empiler(Pile,Val):
    if( ( (Pile[0] < 1) or (Pile[0] == len(Pile))) ):
        print("La pile est pleine ou mal définie !")
        return(False)
    else:
        Pile[Pile[0]] = Val                 # Copie l'élément Val à la case mémoire sélectionné par l'index courant.
        Pile[0] = Pile[0] + 1               # Modification de l'index pour permettre le stockage du prochain élément à empiler.
        return(True)

def PileVide(Pile):
    return(Pile[0] <= 1)

def Depiler(Pile):
    Val = None
    if( PileVide(Pile) != True ):
        Pile[0] = Pile[0] - 1
        Val = Pile[0]                    # Copie l'élément à dépiler dans une variable locale
    return(Val)                          # Retourne la valeur copiée ou la valeur None si pile vide.

def VerificationPar(Expression):
    Val = None
    P = CreaStack(len(Expression))
    for i in range (0,len(Expression), 1):
        if(Expression[i] == "(" ):
            Empiler(P,"o")
        elif(Expression[i] == ")" ):
            if( Depiler(P) == None ):
                print("erreur pile :", P)
                return(False)
        print(P)
    return( (P[0] == 1) )



Math = input("Saisir l'expression mathématique à vérifier : ")

if(VerificationPar(Math) == True):
    print("L'expression mathématique semble cohérente !")
else:
    print("L'expression mathématique est incohérente !")
