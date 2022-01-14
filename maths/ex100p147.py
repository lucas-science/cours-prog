def baleine():
    u = 3000
    n = 0
    while u>=2000:
        u = 0.95*u+76
        n=n+1
    return(2019+n)

print(baleine())