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


def calcul(operation:str,x,y):
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

formule = "3+6*5/4+ "

formule = "((3+2)*6)/5+4"

NUMBER = ["0","1","2","3","4","5","6","7","8","9"]
OPERATEUR = ['+','-','*','/']

PILE2 = CREER_PILE()

def formuleTOnpi(inp):
    res = 0
    op = ""
    for i in inp:
        if i in NUMBER:
            Push(PILE2,float(i))
        if i in NUMBER and op != "":
            Push(PILE2,op)
            op = ""
        if i in OPERATEUR:
            op = i
    return PILE2
    
#print(formuleTOnpi(str(input("rentrer une formule voulu : "))))

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



#print(Evaluation(str(input('entrer une frormule NPI : '))))



"""
def Hanoi(X,n,depart,arrivee,intermediaire):
    if n == 0:
        for i in range(X,0,-1):
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
        return Hanoi(X,n,depart,arrivee,intermediaire)
        
        
pile1 = CreaStack()
pile2 = CreaStack()
pile3 = CreaStack()
N = 0
X = 3
print(Hanoi(X,N,pile1,pile2,pile3))
print(N)
"""

def hanoi(n, depart, intermediaire, arrive):
    if n > 0:
        # move tower of size n - 1 to helper:
        hanoi(n - 1, depart, arrive, intermediaire)
        print("au debut")
        # move disk from source peg to target peg
        if depart:
            Push(arrive,Pop(depart))
            print("dans le if")
        # move tower of size n-1 from helper to target
        hanoi(n - 1, intermediaire, depart, arrive)
        print("a la fin")


pile1 = CreaStack()
for i in range(int(input("entre la taille de la tour : ")),0,-1):
    Push(pile1,i)
print(pile1) 

pile2 = CreaStack()
pile3 = CreaStack()

hanoi(len(pile1),pile1,pile2,pile3)

print(pile1, pile2, pile3)