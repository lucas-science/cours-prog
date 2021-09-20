def iteratif(x,n):
    y = 1
    for i in range(n):
         y = y*x
    return y

print(iteratif(2,4))


def recurs(x,n):
    if n <= 1:  # si n <= 0 alors return 1
        return x
    else:
        return x*recurs(x,n-1)

print(recurs(3,2))