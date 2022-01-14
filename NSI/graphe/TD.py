# ACT 1

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

G = GrapheSurpprimerSommet(G,'A')
print(G)
