# ACT 1
from operator import truediv
from this import d
from numpy import Infinity


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

###################################
# ACT 1

def GrapheNbSommets(g):
    return len(g)


lenG1 = GrapheNbSommets(G)
lenG2 = GrapheNbSommets(G)
print(lenG1,lenG2)

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
#print("Degré A :",degA,"\nDegré B :",degB)


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

#print(GrapheOrienteNbDegre(G,'A'))

# ACT 4
GrMat = {'A':['B','D'],'B':['A','C'],'C':['B'],'D':['A','B']}
def GrapheMatriceAdj(g):
    NbSom = len(g.keys())
    Sommets = []
    Mat = [[ n*0 for n in range(NbSom)] for i in range(NbSom)]
    print(Mat)
GrapheMatriceAdj(GrMat)