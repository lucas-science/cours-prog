# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 15:52:43 2020

@author: mfb
"""
Expression = []                             # Chaîne de caractères contenant l'expression mathématique
cmpt = 0

# Création d'une pile sans taille définie
def CreaStack():
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

def Calcul(Operation, Op1, Op2):
    if(Operation == "+"):
        Result = (Op1 + Op2)
    elif(Operation == "-"):
        Result = (Op1 - Op2)
    elif(Operation == "/"):
        Result = (Op1 / Op2)
    else:
#        try:
#            assert (Operation == "*")
#            Result = (Op1 * Op2)
#        except AssertionError :
#            print("Opérateur inconnu !")
#            print("Interruption du programme !")
        assert (Operation == "*"), "Opérateur inconnu !"     # Traitement des erreurs en cas de mauvais opérateur
        Result = (Op1 * Op2)
    return (Result)

def Operateur(Car):
    return(Car == "+" or Car == "-" or Car == "*" or Car == "/")


def Evaluation(Expr,P):
    Val1 = 0
    Val2 = 0
    op = ""
    Car = str("")
    for i in range(len(Expr)):
        if( (Operateur(Expr[i]) == False) and ((Expr[i] != " ")) ):
             Car = Car + (Expr[i])
        else:
            if( ((Expr[i] == " ") and Car != "") or ((Operateur(Expr[i]) == True) and Car != "" )):
                EmpilerBis(P,str(Car))
                print(str(Car))
                Car = str("")                       # La chaine de caractère est RAZ
                print(P)
            
            if( (Operateur(Expr[i]) == True) and Car == ""):
                Op = Expr[i]
                Val2 = float(DepilerBis(P))
                Val1 = float(DepilerBis(P))
                print("Val 1 = ", Val1)
                print("Val 2 = ", Val2)
                Resultat = Calcul(Op,Val1,Val2)
                EmpilerBis(P,str(Resultat))                           
                print(P)
    return(DepilerBis(P) )


P = CreaStack()


MathNPI = str(input("Saisir l'expression mathématique en NPI à calculer : "))
res = Evaluation(MathNPI,P)
print("Le résultat est :", res)
print("Etat de la pile", P)
