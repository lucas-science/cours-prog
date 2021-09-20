from timeit import default_timer
import matplotlib.pyplot as plt
from random import randint
#from tqdm import tqdm

def minimum(a,b):
    if a < b:
        return (a)
    else:
        return (b)

"""def getmini_recursive2(l):
    if len(l) <= 1:
        return l[0]
    else:
        return getmini_recursive2( minimum(l[0],l[1]) + l[2:])"""
L = [14,8,12,4,5,-40,2]
def getmini_recursive(l):
    if len(l) <= 1:
        return l[0]
    else:
        return minimum(l[0],getmini_recursive(l[1]))

def getmini_iterative(l,base_mini):
    for i in l:
        if i < base_mini:
            base_mini = i
    return base_mini

print(getmini_recursive(L))


def get_data(n):
    L = [ randint(0,10) for x in range(n)]
    mini = L[0]

    start1 = default_timer()
    Resultat_iterative = getmini_iterative(L, mini)
    duration1 = default_timer() - start1

    start2 = default_timer()
    Resultat_recursive = getmini_iterative(L, mini)
    duration2 = default_timer() - start2

    """print({
        "iterative":[
            Resultat_iterative,
            duration1
        ],
        "recursive":[
            Resultat_recursive,
            duration2
        ]
    })"""
    return {
        "iterative":[
            Resultat_iterative,
            duration1
        ],
        "recursive":[
            Resultat_recursive,
            duration2
        ]
    }



"""
dataIterative = []
dataRecursive = []
x = 0
for i in tqdm(range(1000)):
    x+=1
    r = get_data(x)
    dataIterative.append(r["iterative"][1])
    dataRecursive.append(r["recursive"][1])
plt.plot(dataIterative)
plt.plot(dataRecursive)
plt.show()
plt.savefig('recursive_VS_iterative.png')"""