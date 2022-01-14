
"""

#calculer les n premiers termes
L = []
n = int(input("Combien de premier terme voulez vous calculer"))
for i in range(n+1):
    u = i**2 +3*i-4
    L.append(u)

#faire la somme des n termes dans la liste
somme = 0
for x in L:
    somme += x

print("La somme : ", somme,'\n', "La liste : ", L)

"""

#calculer les n premiers termes
L = []
n = int(input("Combien de premier terme voulez vous calculer"))
lastu = 1
for i in range(n+1):
    u = lastu**2 + 4
    L.append(u)
    lastu = u

#faire la somme des n termes dans la liste
somme = 0
for x in L:
    somme += x

print("La somme : ", somme,'\n', "La liste : ", L)