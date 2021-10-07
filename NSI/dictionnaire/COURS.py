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


for i in dico.keys():
    print(i)