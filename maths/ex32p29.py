from matplotlib.pyplot import *

def liste_termes_u(n,a):
    u = a
    L = [u]
    for i in range(1,n+1):
        print(i)
        u = (3*u)/(1+2*u)
        L.append(u)
    return L

L1 = liste_termes_u(10,0.7)


plot(L1, 'b.')

show()
