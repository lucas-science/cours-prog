def terme_u(n=4):
    u = 0
    for k in range(1,n+1):
        u=5*u-1
        print(u)
    return u

print(terme_u())