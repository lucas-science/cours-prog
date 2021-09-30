def CREER_LISTE_VIDE(n):
    L=[None]*(n+1) #Création de liste vide
    L[0]=0 #On initialise la case 0 à 0 éléments
    return L

L = CREER_LISTE_VIDE(6)

def INSERER(l,e,i):
    if (l[0] == (len(l)-1))or (i-1>l[0]):
        print("La liste est pleine ou l'index i n'est pas correct")
        return False
    else:
        for k in range(l[0]+1,i,-1):
            l[k]=l[k-1]
        l[i] = e
        l[0] = l[0]+1
        return True

def SUPPRIMER(l,i):
    if (l[0]!=0) and (i<=l[0]):
        for k in range(i,l[0]):
            l[k] = l[k+1]
        l[0]=L[0]-1
        l[l[0]+1] = None
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

"""
INSERER(L,3,1)
INSERER(L,7,2)
INSERER(L,1,3)
INSERER(L,8,4)
print("insérer : ",L)
SUPPRIMER(L,2)
print("suprimer : ",L)
INSERER(L,15,3)
print("insérer : ",L)

print("recherche : ",RECHERCHER(L,15))

print("indexer 1 : ",INDEXER(L,1))
print("indexer 4 : ",INDEXER (L,4))
print("indexer 10 : ",INDEXER (L,10))

print(MODIFIER(L,25,2), " la liste : ", L)
print(MODIFIER(L,25,10), " la liste : ", L)

"""
#ACT 7
def CREER_PILE_VIDE(n):
    p=[]
    p=[None]*(n+1) #Création de liste vide
    p[0]=1 #On initialise la case 0 à 1
    return p

PILE = CREER_PILE_VIDE(6)


def EMPILER(P,E):
    if P[0] == len(P):
        print("La pile est pleine")
        return False
    else:
        P[P[0]] = E
        P[0] += 1
        return True
#ACT 8
def DEPILER(P):
    if P[0] <= 1:
        print("La pile est vide")
        return False
    else:
        P[0] = P[0]-1
        return P[P[0]]

"""
print(PILE)
EMPILER(PILE,3)
EMPILER(PILE,7)
EMPILER(PILE,1)
EMPILER(PILE,8)
print(PILE)

print( DEPILER(PILE))
"""
print("here")
#ACT 9

def CreaStack():
    return []

def Vide(p):
    if len(p)==0:
        return True
    else:
        return False

def Push(p,x):
    p.append(x)

def Pop(p):
    if len(p)>0:
        return p.pop()
    else:
        print("La PILE est vide")

PILE2 = CreaStack()

print(PILE2)
Push(PILE2, 3)
Push(PILE2, 7)
Push(PILE2, 1)
Push(PILE2, 8)
print(PILE2)

Pop(PILE2)
Pop(PILE2)
print(PILE2)

# ACT 10
"""
def CREER_FILE_VIDE(n):
    F=[None]*(n+3) #Création de liste vide
    F[0]=3 
    F[1]=3
    F[2]=0
    return F

def ENFILER(F,E):
    if F[2]== len(F)-3:
        print("La file est pleine")
        return False
    else:
        F[F[1]]=E
        if F[1]==len(F)-1:
            F[1]=3
        else:
            F[1]+=1
            F[2]+=1
        return True

File=CREER_FILE_VIDE(6) #On créé une liste vide de 6 éléments
print(File)
ENFILER(File,3)
ENFILER (File,7)
ENFILER (File,1)
ENFILER (File,8)
print(File)
print("here2")

#ACT 11
"""
"""
def DEFILER(F):
    if len(F)==0:
        print("La file est vide")
    else:
        Element = F[F[0]]
        if F[0] == len(F)-1:
            F[0]=3
        else:
            F[0]+=1
            F[2]-=1
        return Element

ENFILER(File,8)
print(DEFILER(File))
print(DEFILER(File))
print(File)
"""
# ACT 12
"""
def CreaQueue():
    return []

def QueueEmpty(F):
    if len(F)==0:
        return True
    else:
        return False

def EnQueue(F,x):
    F.append(x)

def Dequeue(F):
    if QueueEmpty(F) == False:
        F.pop(0)
        return "value poped"
    else:
        return("la liste est vie")

FILE3 = CreaStack()

for i in range(5):
    EnQueue(FILE3,2*i)

print(FILE3)
a=Dequeue(FILE3)
print(a)
print(FILE3)
print(QueueEmpty(FILE3))
"""