# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 10:22:45 2020

@author: mfb
"""

def CreaQueue():
    F = []
    return(F)
    
def QueueEmpty(File):
    return(File == [])

def EnQueue(File,Val):
    return(File.append(Val))                    # La méthode .append() sans paramètre -> empile l'élément au sommet de la pile    


def DeQueue(File):
    assert not QueueEmpty(File), "Queue empty !"
    return(File.pop(0))                         # Retourne toujours le contenu du 1er index (index = 0) et le supprime

def QueueSize(File):
    return(len(File))

def QueueTop(Queue):
    assert not QueueEmpty(Queue), "Impossible, la file est vide !"
    return(QueueSize(Queue)-1)     


F = CreaQueue()
print("Taille de la file : ",QueueSize(F))
#QueueTop(F)
print("La pile est-elle vide ? ", QueueEmpty(F))
for i in range(5):
    EnQueue(F,2*i)
print(F)
a = DeQueue(F)
print(a)
print(F)
print("La pile est-elle vide ? ", QueueEmpty(F))
print("Taille de la file : ",QueueSize(F))
print("Index du dernier élément à sortir : ",QueueTop(F))