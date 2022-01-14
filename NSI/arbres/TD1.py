from typing import List


Arbre1 = (8,(4,(3,None,None),(6,None,None)),(12,(9,None,None),(14,None,None)))

Arbre2 = (2,(1,(0,None,None),None),(5,(4,(3,None,None),None),
(12,(9,(8,(6,None,(7,None,None)),None),
(10,None,(11,None,None))),(13,None,(14,None,(18,(17,(15,None,(16,None,None)),
None),(19,None,None)))))))
#print(Arbre2)


def TailleArbre(T:tuple):
    if T != None:
        x = T
        return 1+TailleArbre(x[1]) + TailleArbre(x[2])
    else:
        return 0
 

#print(TailleArbre(Arbre2))

def HauteurArbre(T:tuple):
    if T != None:
        x = T
        return 1+max(HauteurArbre(x[1]) ,HauteurArbre(x[2]))
    else:
        return 0
    
#print(HauteurArbre(Arbre2))


def NombreFeuilles(T:tuple):
    x = T
    if x[1] != None and x[2] !=None:
        return 0 + NombreFeuilles(x[1]) + NombreFeuilles(x[2])
    else:
        return 1

#print(NombreFeuilles(Arbre1))
L1=[]
def HauteurArbrePrefixe(T:tuple,L:list):
    if T!= None:
        x = T
        L.append(x[0])
        HauteurArbrePrefixe(x[1],L)
        HauteurArbrePrefixe(x[2],L)

#HauteurArbrePrefixe(Arbre1,L1)
#print(L)

def HauteurArbreInfixe(T:tuple,L:list):
    if T!= None:
        x = T
        HauteurArbreInfixe(x[1],L)
        L.append(x[0])
        HauteurArbreInfixe(x[2],L)
"""
L2=[]
HauteurArbreInfixe(Arbre1,L2)
print(L2)
L2=[]
HauteurArbreInfixe(Arbre2,L2)
print(L2)"""

def HauteurArbreSuffixe(T:tuple,L:list):
    if T!= None:
        x = T
        HauteurArbreSuffixe(x[1],L)
        HauteurArbreSuffixe(x[2],L) 
        L.append(x[0])

"""
L3=[]
HauteurArbreSuffixe(Arbre1,L3)
print(L3)
L3=[]
HauteurArbreSuffixe(Arbre2,L3)
print(L3)"""


def CreateFile():
    return []

def Enfiler(x,f:list):
    f.append(x)

def Defiler(f:list):
    return f.pop(0)


def ParcoursArbreLargeur(T,f,l:list):
    Enfiler(T,f)
    while f != []:
        x = Defiler(f)
        l.append(x[0])
        if x[1] != None:
            Enfiler(x[1],f)
        if x[2] != None:
            Enfiler(x[2],f)

F = CreateFile()
L4 = []
ParcoursArbreLargeur(Arbre2,F,L4)
print(L4)
<<<<<<< HEAD
=======
"""
>>>>>>> 79c3e92231570e12a84dde0cbff63c94dbdb6f2a
"""
F = CreateFile()
Enfiler(Arbre1,F)
x = Defiler(F)
print(x[0])
"""
