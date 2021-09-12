from timeit import default_timer
import matplotlib.pyplot as plt
from random import randint
from tqdm import tqdm


def getmini_iterative(l,base_mini):
    for i in l:
        if i < base_mini:
            base_mini = i
    return base_mini



def getmini_recursive(l,base_mini):
    if len(l) <= 1:
        return base_mini
    else:
        if base_mini < l[0]:
            return getmini_recursive(l[1:],base_mini)
        else:
            base_mini = l[0]
            return getmini_recursive(l[1:],base_mini)



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

dataIterative = []
dataRecursive = []
x = 0
for i in tqdm(range(10000)):
    x+=1
    r = get_data(x)
    dataIterative.append(r["iterative"][1])
    dataRecursive.append(r["recursive"][1])


plt.plot(dataIterative)
plt.plot(dataRecursive)
plt.show()
plt.savefig('recursive_VS_iterative.png')