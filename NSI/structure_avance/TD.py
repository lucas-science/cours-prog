

from os import putenv


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
L1=CREER_LISTE_VIDE(5)
L2=CREER_LISTE_VIDE(5)
INSERER(L1,0,1)
INSERER(L1,1,2)
INSERER(L1,2,3)
INSERER(L1,3,4)
INSERER(L1,4,5)
INSERER(L2,INDEXER(L1,1),1)
INSERER(L2,INDEXER(L1,2),1)
INSERER(L2,INDEXER(L1,3),1)
INSERER(L2,INDEXER(L1,4),1)
INSERER(L2,INDEXER(L1,5),1)
print(L1,L2)
"""

def CREER_PILE_VIDE(n):
    p=[]
    p=[None]*(n+1) #Création de liste vide
    p[0]=1 #On initialise la case 0 à 1
    return p



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
Pile=CREER_PILE_VIDE(5)
EMPILER(Pile,'K')
EMPILER(Pile,'A')
EMPILER(Pile,'Y')
EMPILER(Pile,'A')
EMPILER(Pile,'K')
DEPILER(Pile)
DEPILER(Pile)
DEPILER(Pile)
DEPILER(Pile)
EMPILER(Pile,'O')
EMPILER(Pile,'*')
EMPILER(Pile,'*')
EMPILER(Pile,'*')
EMPILER(Pile,'*')
print(Pile)
"""
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
        F[2]+=1
        F[F[1]]=E
        if F[1]==len(F)-1:
            F[1]=3
        else:
            F[1]+=1
        return True

def DEFILER(F):
    if len(F)==0:
        print("La file est vide")
    else:
        F[2]-=1 #MODIFFFFF
        Element = F[F[0]]
        if F[0] == len(F)-1:
            F[0]=3
        else:
            F[0]+=1
        return Element
"""
"""
File=CREER_FILE_VIDE(5)
ENFILER(File,'K')
ENFILER(File,'A')
ENFILER(File,'Y')
ENFILER(File,'A')
ENFILER(File,'K')
DEFILER(File)
DEFILER(File)
DEFILER(File)
DEFILER(File)
ENFILER(File,'*')
ENFILER(File,'*')
ENFILER(File,'*')
ENFILER(File,'O')
ENFILER(File,'*')
print(File)
"""
def CREER_PILE():
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

PILE = CREER_PILE()

def VERIFIER_PARENTHESE(inp):
    for i in inp:
        if i == "(":
            Push(PILE,i)
            #print(PILE)
        if i == ')' and Vide(PILE):
            return False
        if i == ")" and Vide(PILE)==False:
            Pop(PILE)
            #print(PILE)
    if Vide(PILE):
        return True
    else:
        length = len(PILE)
        for i in range(length):
            Pop(PILE)
        return False

"""print(VERIFIER_PARENTHESE("13*2+(5*6)+10/(5+1)"))
print(VERIFIER_PARENTHESE(")3*(2+1)/(15/6)+6 "))

print(VERIFIER_PARENTHESE(" "))"""

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
        return F.pop(0)
    else:
        return("la liste est vie")


def calcul(operation:str,x:int,y:int):
    if operation == '*':
        return x*y
    elif operation == '/':
        return x/y
    elif operation == '+':
        return x+y
    elif operation == '-':
        return x-y
    else:
        return "'operation' est invalide"
"""
formule = "((3+2)*6)/5+4"

NUMBER = ["0","1","2","3","4","5","6","7","8","9"]
OPERATEUR = ['+','-','*','/']

PILE2 = CreaQueue()

def Evaluation(inp):
    res = 0
    op = ""
    for i in inp:
        if i in NUMBER:
            EnQueue(PILE2,float(i))
            print("la2",PILE2)
        if i in NUMBER and op != "" and len(PILE2) == 2:
            res = calcul(op,Dequeue(PILE2),Dequeue(PILE2))
            EnQueue(PILE2,res)
            print("la2",PILE2)
            op = ""
        if i in OPERATEUR:
            op = i
    return res
    
"""
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

def sommet(p):
    return p[-1]



OPERATEUR = ['+','-','*','/']

def Evaluation(inp):
    pile = CreaStack()
    formule = inp.split(" ")
    print(formule)
    for i in formule:
        if i in OPERATEUR:
            b = Pop(pile)
            a = Pop(pile)
            res = calcul(i,a,b)
            Push(pile,res)
        else:
            Push(pile,float(i))
    return pile[0]



print(Evaluation(str(input('entrer une frormule NPI : '))))

def Hanoi(n,depart,arrivee,intermediaire):
    if n == 0:
        for i in range(n,0,-1):
            Push(depart,i)
    trivialEND = depart.copy()
    if arrivee == trivialEND:
        return True
    else:
        if Vide(intermediaire) and Vide(arrivee):
            Push(arrivee,Pop(depart))
        elif Vide(intermediaire):
            Push(intermediaire,Pop(depart))
        else:
            if sommet(arrivee)<sommet(depart):
                Push(intermediaire,Pop(depart))
                
            elif sommet(arrivee)>sommet(intermediaire):
                Push(arrivee, Pop(intermediaire))   

            elif Vide(depart):
                if sommet(arrivee)>sommet(intermediaire):
                    Push(arrivee,Pop(intermediaire))
                elif sommet(arrivee)<sommet(intermediaire):
                    Push(intermediaire,Pop(arrivee))
        print(depart,arrivee,intermediaire)
        n += 1
        return Hanoi(n,depart,arrivee,intermediaire)
        
        


pile1 = CreaStack()
pile2 = CreaStack()
pile3 = CreaStack()
N = 0
print(Hanoi(N,pile1,pile2,pile3))
print(N)
