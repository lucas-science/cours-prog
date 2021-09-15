from matplotlib.pyplot import *

def liste_termes_u(n,a):
    u = a
    L = [u]
    for i in range(1,n+1):
        u = 4*u-6
        L.append(u)
    return L

L1 = liste_termes_u(5,1)
L2 = liste_termes_u(5,4)
L3 = liste_termes_u(5,2)

plot(L1, 'r.')
plot(L2, 'b.')
plot(L3, 'g.')


show()
