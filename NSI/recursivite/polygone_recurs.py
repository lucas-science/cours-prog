import turtle as t


def doPolygone(n,l,a):
    if n == 0:
        return 1
    else:
        t.width(4)
        t.color('blue')
        t.forward(l)
        t.right(a)
        return doPolygone(n-1,l,a)


N = int(input("rentrer le nombre de côté que votre polygone doit faire : ",))
L = int(input("rentrer la longeur des côtés que votre polynome doit faire : "))

Ang = ((N-2)*180)/N

doPolygone(N,L,180-Ang)

t.exitonclick()

