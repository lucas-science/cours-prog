def INSERER(l,e,i):
    if (l[0] == (len(l)))or (i-1>l[0]):
        print(i-1,len(l)-1)
        print("La liste est pleine ou l'index i n'est pas correct")
        return False
    else:
        l[i] = e
        l[0] = l[0]+1
        return True

def CREER_LISTE_VIDE(n):
    L=[None]*(n+1) #Création de liste vide
    L[0]=0 #On initialise la case 0 à 0 éléments
    return L

L = CREER_LISTE_VIDE(6)


INSERER(L,3,1)
INSERER(L,7,2)
INSERER(L,1,3)
INSERER(L,8,4)

print(L)