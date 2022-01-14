from timeit import default_timer as timer

L=[95, 28, 36, 52, 85, 56, 34, 59, 17, 26, 16, 25, 69, 98, 4, 85, 81, 48, 11, 57]


#   Fonction recursive
cpmt_recurs = 0
def recherche_recurs(l,e,d,f):
    global cpmt_recurs
    cpmt_recurs += 1
    if d == f:
        return l[d] == e
    m = (d+f)//2
    
    return (recherche_recurs(l,e,d,m) or recherche_recurs(l,e,m+1,f))


#   Fonction iterative
cpmt_iterative = 0
def recherche_iterative(l,e):
    global cpmt_iterative
    for i in l:
        cpmt_iterative += 1
        if e == i:
            return True
    return False

print("######### PAS TRIER ############")
print("RECURS")
debut1 = timer()
recherche_recurs(L,25,0,len(L)-1)
fin1 = timer()
print(f"Timer : {fin1-debut1}\nNombre d'appel : {cpmt_recurs}")

print("ITER")
debut2 = timer()
recherche_iterative(L,25)
fin2 = timer()
print(f"Timer : {fin2-debut2}\nNombre d'appel : {cpmt_iterative}")





def tri_selection_min(tableau:list):
    """
    Algorithme de tri par sélection du minimum d'un tableau
    :param tableau: tableau envoyé (list)
    :return: tableau : tableau trié (list)
    """
    for i in range(len(tableau)-1):
        # on enregistre le contenu de la première case
        valeur_origine=tableau[i]
        # on note la position de la valeur minimum
        position_mini=i
        for j in range(i+1,len(tableau)):
            if tableau[j]<tableau[position_mini]:
                position_mini=j
        # permutation des valeurs
        tableau[i]=tableau[position_mini]
        tableau[position_mini]=valeur_origine
    return tableau


L2= tri_selection_min(L)
print(L2)


cpmt_recurs = 0
def rechercheTriee(Liste,x,d,f):
    global cpmt_recurs
    cpmt_recurs += 1
    if (d == f):
        return( Liste[d] == x)
    m = (d+f)//2
    if(Liste[m] >= x):
        return( rechercheTriee(Liste,x,d,m) )
    else:
        return( rechercheTriee(Liste,x,m+1,f) ) 

def recurs(Liste):
    if len(Liste) == 1:
        return Liste[0]
    else:
        return max(Liste[0], recurs(L[1:]))
print("la 1",recurs(L2,85))

print("la",rechercheTriee(L2,85,0,len(L2)-1))
cpmt_iterative = 0
def recherche_iterative(l,e):
    global cpmt_iterative
    for i in l:
        cpmt_iterative += 1
        if e == i:
            return True
    return False
"""
print("######### TRIER ############")
print("RECURS")
debut3 = timer()
rechercheTriee(L2,25,0,len(L2)-1)
fin3 = timer()
print(f"Timer : {fin3-debut3}\nNombre d'appel : {cpmt_recurs}")
print("ITER")
debut4 = timer()
recherche_iterative(L2,25)
fin4 = timer()
print(f"Timer : {fin4-debut4}\nNombre d'appel : {cpmt_iterative}")

"""