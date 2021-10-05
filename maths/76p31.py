def factorielle(n):
    p = 1
    for i in range(2,n+1):
        p*=i
    return p 

print(factorielle(3))


def facto_partielle(n,k):
    p = 1
    for i in range(n,n-k):
        print(i)
    return 1

facto_partielle(5,2)

for i in range(5,2,-1):
    print(i)
