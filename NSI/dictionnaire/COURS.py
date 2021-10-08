Dictionnaire = {"nom": "Duchmol", "prenom": "Gérard", "date naissance":"15/07/2005"}
print(type(Dictionnaire))




# Autre méthode de déclaration
dico = dict()
dico ["nom"] = " Duchmol "
dico ["prenom"] = " Gérard "
dico ["date de naissance"] = "15/07/2005"
dico["lieu de naissance"] =  "Quelque part"
dico["heure naissance"] = "21h53"

print(dico["lieu de naissance"])
print(f'je suis {dico["nom"]}{dico["prenom"]}  né le {dico["date de naissance"]} à {dico["heure naissance"]} ')

print(dico)
del(dico["lieu de naissance"])
print(dico)



magasin = {"Sabre laser" : 229.0, "Etoile ninja" : 29.95, "Cape" : 75.0, "Baguette" : 35.0,
 "Chapeau" : 12.0, "Bandeau" : 12.0, "Balai" : 130.0}

panier1 = {"Sabre laser" : 3, "Balai" : 1, "Chapeau" : 1}

def TotalDu(magasin:dict, panier:dict):
    s = 0
    for (elem,nbr) in panier.items():
        s += nbr*magasin[elem]
    return s

print(TotalDu(magasin,panier1))

def PouvoirAchat(magasin:dict,maxP:int):
    listepossible = []
    for (elem,prix) in magasin.items():
        if prix <= maxP:
            listepossible.append(elem)
    return(f'Avec un capital de {maxP} $ de départ on peut acheter un des éléments suivant : {listepossible}')

print(PouvoirAchat(magasin,30))