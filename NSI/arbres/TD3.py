Arbre1 = [
    15,[
        6,[
            3,[
                2,None,None
            ],[
                4,None,None
            ]
        ],[
            7,None,[
                13,[
                    9,None,None
                ],None
            ]
        ]
    ],[
        18,[
<<<<<<< HEAD
            17,None,None
=======
            17,None,None 
>>>>>>> 79c3e92231570e12a84dde0cbff63c94dbdb6f2a
        ],[
            20,None,None
        ]
    ]
]

<<<<<<< HEAD
def ABR_recherche_noeud(T,e:int):
    if T == None:
        return False
    if e == T[0]:
        return True 
    if e < T[0]:
        return ABR_recherche_noeud(T[1],e)
    elif e > T[0]:
        return ABR_recherche_noeud(T[2],e)

#print(ABR_recherche_noeud(Arbre1,117))

def ABR_RechercheMin(T):
    if T[1] == None:
        return T[0]
    return ABR_RechercheMin(T[1])

#print(ABR_RechercheMin(Arbre1))

def ABR_RechercheMax(T):
    if T[2] == None:
        return T[0]
    return ABR_RechercheMax(T[2])

#print(ABR_RechercheMin(Arbre1))
=======

>>>>>>> 79c3e92231570e12a84dde0cbff63c94dbdb6f2a

def ABR_intertion(a,y):
    arb = a
    while a is not None:
        arb = a
        if y < arb[0]:
            a = arb[1]
        else:
            a = arb[2]
    if y < arb[0]:
        arb[1] = [y,None,None]
        print("inserer y a gauche",Arbre1)
<<<<<<< HEAD
    if y > arb[0]:
        arb[2] = [y,None,None]
        print("inserer y a droite",Arbre1)
    else:
        print("il existe déjà")    

#ABR_intertion(Arbre1,9)
=======
    else:
        arb[2] = [y,None,None]
        print("inserer y a droite",Arbre1)

#ABR_intertion(Arbre1,17.5)

>>>>>>> 79c3e92231570e12a84dde0cbff63c94dbdb6f2a

def ABR_insertion_BIS(a,y):
    arb = a
    if a[1] is not None or a[2] is not None:
        if y <arb[0]:
            a = arb[1]
            ABR_insertion_BIS(a,y)
        else:
            a = arb[2]
            ABR_insertion_BIS(a,y)
    else:
        if y < arb[0]:
            arb[1] = [y,None,None]
<<<<<<< HEAD
        elif y > arb[0]:
            arb[2] = [y,None,None]
        else:
            print("il existe déjà")

#ABR_insertion_BIS(Arbre1,2)
#print(Arbre1)


def ABR_supr(T,k):
    arb = T
    while T is not None:
        arb = T
        if k < arb[0]:
            T = arb[1]
        elif k > arb[0]:
            T = arb[2]
        elif k == arb[0]:
            if arb[1] is None and arb[2] is None:
                arb.clear()
                return None
            else:
                if arb[1] is None:
                    arb[0] = arb[2][0]
                    arb[1] = arb[2][1]
                    arb[2] = arb[2][2]
                    print(arb)
                elif arb[2] is None:
                    arb[0] = arb[1][0]
                    arb[1] = arb[1][1]
                    arb[2] = arb[1][2]
                return None
    if k < arb[0]:
        arb[1] = [k,None,None]
    if k > arb[0]:
        arb[2] = [k,None,None]
print(Arbre1)
print(ABR_supr(Arbre1,20))
print(Arbre1)
=======
        else:
            arb[2] = [y,None,None]

#print(ABR_insertion_BIS(Arbre1,16))
#print(Arbre1)


def ABR_InsertNoeudRecur(a,eti):
    if (a == None):
        return[eti,None,None]
    else:
        r,g,d = a[0],a[1],a[2]
        if(eti == r):
            return[r,g,d]
        elif(eti > r):
            return[r,g,ABR_InsertNoeudRecur(d,eti)]
        else:
            return[r,ABR_InsertNoeudRecur(g,eti),d]

etiquette = int(input("Quel noeud insérer ? "))
AbrModif = ABR_InsertNoeudRecur (Arbre1,etiquette)
print("Nouvel AbrModif : ",AbrModif )
>>>>>>> 79c3e92231570e12a84dde0cbff63c94dbdb6f2a
