def liste_termes_u(p):
    L =[5]
    for k in range(1,p+1):
        L.append(0.5*L[-1]+0.5*(k-1)-1.5)
    return L

print(liste_termes_u(5))
