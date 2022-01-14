from timeit import default_timer as timer

cmpt = 0
cmptdvr = 0

def expo_recursif(x,n):
    global cmpt
    cmpt +=1
    if n<1:
        return 1
    else:
        return (x*expo_recursif(x,n-1))


def expo_recur_dvr(x,n):
    global cmptdvr
    cmptdvr += 1
    if n < 1:
        return 1
    else:
        if n%2 == 0:
            return (expo_recur_dvr(x*x,n//2))
        else:
            return(x*expo_recur_dvr(x*x,n//2))
"""
debut1 = timer()
print(expo_recursif(2,500))
fin1 = timer()
print('delta temps : {}\nnombre d appel recursif : {}'.format(fin1-debut1, cmpt))

print("\n")



debut2 = timer()
print(expo_recur_dvr(2,500))
fin2 = timer()
print('delta temps : {}\nnombre d appel recursif : {}'.format(fin2-debut2, cmptdvr))


"""

L=[95, 28, 36, 52, 85, 56, 34, 59, 17, 26, 16, 25, 69, 98, 4, 85, 81, 48, 11, 57]
cmp1 = 0
cmp2 = 0
def recherche_DPR(l,x,d,f):
    global cmp1
    cmp1 += 1
    if d == f:
        return l[d] == x
    m = (d+f)//2
    return recherche_DPR(l,x,d,m) or recherche_DPR(l,x,m+1,f)

def recherche_iter(l,e):
    global cmp2
    for i in l:
        cmp2 += 1
        if i == e:
            return True
    return False


print(recherche_DPR(L,59,0,len(L)-1))