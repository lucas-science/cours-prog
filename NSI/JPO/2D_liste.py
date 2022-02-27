from random import randint

def pprint(L:list):
    print("[")
    for i in L:
        print("  ",i,",")
    print("]")

# Le tableau sur lequel on travaille
Table = [[randint(1,10) for i in range(5)] for j in range(5)]
pprint(Table)

#Recherche Somme diagonale

def SommeOfList(L:list):
    """
    return la somme d'une list à 1 dimenssion
    """
    somme = 0 
    for i in L:
        somme += i
    return somme

def Liste_Diagonale(L:list):
    """
    return la liste d'élément formant la diagonale
    """
    l = []
    for y in range(len(L)):
        x = y
        l.append(L[y][x])
    return l

def Somme_diagonale(L:list):
    """_summary_
    return la somme des élément formant la diagonale
    """
    l = Liste_Diagonale(L)
    somme = SommeOfList(l)
    return somme

def Liste_Colonne(L:list, colonne:int):
    """
    return la liste d'élément formant la colonne k d'un tableau
    """
    if colonne < 0 or colonne >= len(L):
        return "La colonne renseigné est invalide"
    else:
        l = []
        for y in range(len(L)):
            l.append(L[y][colonne])
        return l

def Somme_Colonne(L:list, colonne:int):
    """
    return la somme des éléments formant la colonne k d'un tableau
    """
    l = Liste_Colonne(L,colonne)
    somme = SommeOfList(l)
    return somme


# On appel les fonctions précédentes 

print("#### Travaille sur la diagonale du tableau ####")
print("Liste : ",Liste_Diagonale(Table))
print("Somme : ",Somme_diagonale(Table))

colonne = 3
print(f"\n#### Travaille sur la colonne {colonne} ####")
print("Liste : ",Liste_Colonne(Table,colonne))
print("Somme : ",Somme_Colonne(Table,colonne))