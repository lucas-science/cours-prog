# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 21:27:52 2020

@author: mfb
"""

import turtle as t

##t.setup(1000,1000)
t.color("red")
#¶t.pensize(10)
t.width(10)
t.begin_fill()
t.speed(1)

def PolygonIteratif(n,lg,angle):
#    angle= 180 - ((n-2)*180/n)
#    print(angle)
    for i in range(n):
        t.forward(lg)
        t.right(angle)
    return    


def PolygonRecursif(n,lg,angle):
    if(n < 1):
        t.forward(lg)
        return 1
    else:
        PolygonRecursif(n-1,lg,angle)
        t.right(angle)
        t.forward(lg)


nbCote = int(input("saisir le nombre de cotés :"))
lgCote = int(input("saisir la longueur d'un côté :"))
angle= 180 - ((nbCote-2)*180/nbCote)

#PolygonIteratif(nbCote,lgCote)
PolygonRecursif(nbCote,lgCote,angle)

t.exitonclick()