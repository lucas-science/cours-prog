def CREER_LISTE_VIDE(n):
    L=[None]*(n+1) #Création de liste vide
    L[0]=0 #On initialise la case 0 à 0 éléments
    return L

L = CREER_LISTE_VIDE(6)

def INSERER(l,e,i):
    if (l[0] == (len(l)))or (i-1>l[0]):
        print("La liste est pleine ou l'index i n'est pas correct")
        return False
    else:
        for k in range(l[0]+1,i+1,-1):
            l[k]=l[k-1]
        l[i] = e
        l[0] = l[0]+1
        return True

def SUPPRIMER(l,i):
    if (l[0]!=0) and (i<=l[0]):
        for k in range(i,l[0]):
            l[k] = l[k+1]
        l[i] = None
        l[0]=L[0]-1
        return True
    else:
        print("La liste est vide ou l'index i n'est pas correct")
        return False


def RECHERCHER(l,e):
    for i in l:
        if i == e:
            return l.index(i)
    return -1
    

def INDEXER(l,i):
    if (i>=1) and (i<=l[0]):
        return l[i]
    else:
        return "L'index i est incorrecte"

def MODIFIER(l,e,i):
    if (i>=1) and (i<=l[0]):
        l[i] = e
        return True
    else:
        return "L'index i est incorrecte"


def LONGUEUR(l):
    return l[0]

INSERER(L,3,1)
INSERER(L,7,2)
INSERER(L,1,3)
INSERER(L,8,4)

print(L)
SUPPRIMER(L,3)
INSERER(L,15,3)
print(L)

print(RECHERCHER(L,15))

print(INDEXER(L,1))
print(INDEXER (L,4))
print(INDEXER (L,10))

print(MODIFIER(L,25,2), "\n"+"la liste : ", L)
print(MODIFIER(L,25,10), "\n"+"la liste : ", L)

