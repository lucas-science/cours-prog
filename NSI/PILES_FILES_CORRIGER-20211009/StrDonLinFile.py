# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 10:22:45 2020

@author: mfb
"""

def Creer_File_Vide(n):
    F = []
    [F.append(None) for i in range(n+3)]
    F[0] = 3                    # Index de la tête de file
    F[1] = 3                    # Index de la queue de file
    F[2] = 0                    # Taille de la file : A l'initialisation la file est vide !
    return(F)
    


def Enfiler(File,Val):
    if( ( (File[2] >= len(File)-3)) ):
        print("La File est pleine !")
        return(False)
    else:
        File[File[1]] = Val
        File[2] = File[2] + 1
        if( File[1] < len(File)-1 ):
            File[1] = File[1] + 1
        else:
            File[1] = 3            
        return(True)

def Defiler(File):
    if( (File[2] < 1) ):
        print("La File est vide !")
        return(False)
    else:
        Val = File[File[0]]
        File[2] = File[2] - 1
        if( File[0] < len(File)-1):
            File[0] = File[0] + 1
        else:
           File[0] = 3            
        return(Val)
        


F = Creer_File_Vide(5)
print(F)
Enfiler(F,"K")
print(F)
Enfiler(F,"A")
print(F)
Enfiler(F,"Y")
print(F)
Enfiler(F,"A")
print(F)
Enfiler(F,"K")
print(F)
print(Defiler(F))
print(F)
print(Defiler(F))
print(F)
print(Defiler(F))
print(F)
print(Defiler(F))
print(F)
Enfiler(F,"*")
print(F)
Enfiler(F,"*")
print(F)
Enfiler(F,"*")
print(F)
Enfiler(F,"O")
print(F)
Enfiler(F,"*")
print(F)