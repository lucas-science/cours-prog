# ACT 1

import random


def GrapheCreation():
    return dict()

G = GrapheCreation()


# ACT 2
def GrapheAjoutSommet(g,s):
    if s not in g:
        g[s] = list()
        return g
    else:   
        print("le sommet existe déjà")
        return g

G = GrapheAjoutSommet(G,"A")
G = GrapheAjoutSommet(G,"B")
G = GrapheAjoutSommet(G,"C")
G = GrapheAjoutSommet(G,"D")
G = GrapheAjoutSommet(G,"E")
G = GrapheAjoutSommet(G,"F")
G = GrapheAjoutSommet(G,"F")

print(G)

# ACT 3

def GrapheAjouterArcs(g,sd,sf):
    if sf not in g[sd]:
        g[sd].append(sf)
        return g
    else:
        print("arcs déjà ajouté")
        return g 

G = GrapheAjouterArcs(G,'A','B')
G = GrapheAjouterArcs(G,'B','C')
G = GrapheAjouterArcs(G,'C','D')
G = GrapheAjouterArcs(G,'E','D')
G = GrapheAjouterArcs(G,'F','E')

print(G)

# ACT 4
print("lol")
def GrapheAjouterArete(g,sd,sf):
    if sf not in g[sd]:
        g[sd].append(sf)
    if sd != sf and sd not in g[sf]:
        g[sf].append(sd)
    return g

G2 = GrapheCreation()
G2 = GrapheAjoutSommet(G,"A")
G2 = GrapheAjoutSommet(G,"B")
G2 = GrapheAjoutSommet(G,"C")
G2 = GrapheAjoutSommet(G,"D")
G2 = GrapheAjoutSommet(G,"E")
G2 = GrapheAjoutSommet(G,"F")
G2 = GrapheAjoutSommet(G,"F")


G2 = GrapheAjouterArete(G2,'A','B')
G2 = GrapheAjouterArete(G2,'A','C')
G2 = GrapheAjouterArete(G2,'A','D')
G2 = GrapheAjouterArete(G2,'B','C')
G2 = GrapheAjouterArete(G2,'B','D')
G2 = GrapheAjouterArete(G2,'C','D')


print(G2)
print("lol")

# ACT 5

def GrapheSurpprimerSommet(g,Snom):
    if Snom in g:
        del(g[Snom])
        for sommet,val in g.items():
            if Snom in val:
                index = val.index(Snom)
                del val[index]
        return g
    else:
        print("ce sommet n'existe pas")
        return g

#G = GrapheSurpprimerSommet(G,'A')
print(G)


# ACT 6

def GrapheSupprimerArc(g,sd,sf):
    if sd in g and sf in g[sd]:
        index = g[sd].index(sf)
        del g[sd][index]
        return g
    else:
        print("imposible de supprimer cette arc")
        return g

#G = GrapheSupprimerArc(G,'A','B')
#G = GrapheSupprimerArc(G,'E','A')

print(G)

print("lol")
# ACT 7

def GrapheSupprimerArete(g,sd,sf):
    if sd in g and sf in g[sd]:
        index = g[sd].index(sf)
        del g[sd][index]
        if sd != sf:
            index = g[sf].index(sd)
            del g[sf][index]
        return g
    else:
        print("impossible de supprimer l'arrête")
        return g
print(G)

G = GrapheSupprimerArete(G,'A','B')
G = GrapheSupprimerArete(G,'E','A')

print(G)

print("###################")

###############################################################################


# ACT 1

def GrapheNbSommets(g):
    return len(g)


lenG1 = GrapheNbSommets(G)
lenG2 = GrapheNbSommets(G)
print("Nombre Sommets G1 :",lenG1,"\nNombre Sommets G2 :",lenG2)

# ACT 2

def GrapheNonOrienteNbDegre(g,s):
    if s in g:
        if g[s] != []:
            return len(g[s])
        else:
            return 0
    else:
        print("sommet inexistant mon gaté")
        return "error"

degA = GrapheNonOrienteNbDegre(G2,'A')
degB = GrapheNonOrienteNbDegre(G2,'C')
print("Degré A :",degA,"\nDegré B :",degB)

# ACT 3 
def GrapheOrienteNbDegre(g,s):
    deg = 0
    if s in g:
        if g[s] != []:
            deg = len(g[s])
        for i in g.keys():
            if s in g[i] and i != s:
                deg += 1
    else:
        return "sommet inexistant"
    return "Le sommet {} a pour degré : {}".format(s,deg)

print(GrapheOrienteNbDegre(G,'A'))

# ACT 4
GrMat = {'A':['B','D'],'B':['A','C'],'C':['B'],'D':['A','B']}
def GrapheMatriceAdj(g):
    NbSom = len(g.keys())
    Sommets = []
    Mat = [[ n*0 for n in range(NbSom)] for i in range(NbSom)]
    
    sortKey = sorted(g.keys())
    for k in sortKey:
        Sommets.append(k)
    
    for clef in g:
        lval = g.get(clef)
        lval.sort()
        index_ligne = Sommets.index(clef)
        for i in lval:
            index_colonne = Sommets.index(i)
            Mat[index_ligne][index_colonne] = 1
    return Mat

def beautyPrint(l):
    print("[")
    for i in l :
        print("  ",i)
    print("]")

Mat1 = GrapheMatriceAdj(GrMat)
Mat2 = GrapheMatriceAdj(G)
beautyPrint(Mat1)
beautyPrint(Mat2)

# ACT 5

Graphe = GrapheCreation()

Graphe = GrapheAjoutSommet(Graphe,'A')
Graphe = GrapheAjoutSommet(Graphe,'B')
Graphe = GrapheAjoutSommet(Graphe,'C')
Graphe = GrapheAjoutSommet(Graphe,'D')
Graphe = GrapheAjoutSommet(Graphe,'E')
Graphe = GrapheAjoutSommet(Graphe,'F')
Graphe = GrapheAjoutSommet(Graphe,'G')
Graphe = GrapheAjoutSommet(Graphe,'H')

Graphe = GrapheAjouterArete(Graphe,'A','C')
Graphe = GrapheAjouterArete(Graphe,'A','B')
Graphe = GrapheAjouterArete(Graphe,'C','H')
Graphe = GrapheAjouterArete(Graphe,'H','G')
Graphe = GrapheAjouterArete(Graphe,'G','F')
Graphe = GrapheAjouterArete(Graphe,'F','E')
Graphe = GrapheAjouterArete(Graphe,'E','B')
Graphe = GrapheAjouterArete(Graphe,'E','D')
Graphe = GrapheAjouterArete(Graphe,'D','B')

def CreateFILE():
    return []
def Enqueue(f,e):
    return f.append(e) 
def Dequeue(f):
    return f.pop(0)

def GraphBFS(G,S):
    D = {S:None}
    print(D)
    Q = CreateFILE()
    Enqueue(Q,S)
    while Q != []:
        u = Dequeue(Q)
        for v in G[u]:
            if v in D:
                continue
            D[v] = u
            Enqueue(Q,v)
    return D

print(GraphBFS(Graphe,'C'))

# ACT 6 
def connexeOrNot(G):
    listKey1 = []
    for i in Graphe.keys():
        listKey1.append(i)
    bfs = GraphBFS(G,listKey1[0])
    listKey2 = []
    for y in Graphe.keys():
        listKey2.append(y)
    #print(listKey2,listKey1)
    if len(listKey1) == len(listKey2):
        return "is connexe"
    else:
        return "is'nt connexe"
G2= {'A' :['E','F'],'B' :['C','D'],'C' :['D','B'],'D' :['B','C'],'E' :['A'],'F':['A']}
print(connexeOrNot(G2))

# ACT 7
def CreatePile():
    return []
def empiler(f,e):
    return f.append(e)
def depiler(f):
    return f.pop()

def GrapheDFS(g,s):
    D = {s:None}
    Q = CreatePile()
    empiler(Q,s)
    while Q != []:
        u = Q[-1]
        R = g.get(u)
        if R != []:
            v = random.choice(R)
            R.remove(v)
            D[v] = u
            empiler(Q,v)
        else:
            depiler(Q)
    return D

GrL={'A':['B','C'],'B':['A','D','E'],'C':['A','D','H'],'D':['B','C','E'],'E':['B','D','F'],'F':['E','G'],'G':['F','H'],'H':['G','C'] } 
print("------------------")
print(GrapheDFS(GrL,'C'))
print("------------------")

# ACT 8
def MatriceAdjGraphe(M):
    Graphe = {}
    asciinum = 65
    lettre = []
    for i in range(len(M)):
        lettre.append(chr(asciinum+i))

    for l in lettre:
        Graphe = GrapheAjoutSommet(Graphe,l)

    for k in range(len(M)):
        for j in range(len(M)):
            if M[k][j] == 1:
                Graphe = GrapheAjouterArcs(Graphe,lettre[k],lettre[j])
    return Graphe


grMat = [
    [0,1,0,1,1],
    [1,0,1,0,0],
    [0,1,0,1,1],
    [1,0,1,0,0],
    [1,0,1,0,1]
]
#print("#######################")
#print(MatriceAdjGraphe(grMat))
