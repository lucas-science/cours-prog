from unittest import TestSuite
from sympy import true
from ComplexStruct import PPile, FFile

pile = PPile()

class Noeud():
    def __init__(self,e):
        self.clef = e

class Arbre(): 
    def __init__(self,r) -> None:
        #Noeud.__init__(self,r)
        self.racine = Noeud(r)
        self.Sag = None
        self.Sad = None
        self.taille = None
        self.hauteur = None

        self.taille = 0
    def getArbre(self):
        return [self.racine,self.Sag,self.Sad]

    def __Taille__(self,a):
        if a == None:
            return 0
        else:
            return 1+self.__Taille__(a.Sag)+self.__Taille__(a.Sad)
        
    def GetTaille(self):
        self.taille = self.__Taille__(self)
        return self.taille

    def __hauteur__(self,a):
        if a == None:
            return 1
        else:
            return max(self.__Taille__(a.Sag),self.__Taille__(a.Sad))-1

    def GetHauteur(self):
        self.hauteur = self.__hauteur__(self)
        return self.hauteur

    def BFS(self):
        lst = []
        if self.Sag != None and self.Sad != None:
            f = FFile()
            f.Enfiler(self)
            while f.Est_Vide() == False:
                arbre_courant = f.Defiler()
                lst.append(arbre_courant.racine.clef)
                if arbre_courant.Sag != None:
                    f.Enfiler(arbre_courant.Sag)
                if arbre_courant.Sad != None:
                    f.Enfiler(arbre_courant.Sad)
        return lst
    
    def ParcoursPrefixe(self,a=True):
        if a == True:
            a = self
        if a != None:
            return ([a.racine.clef]+self.ParcoursPrefixe(a.Sag)+ self.ParcoursPrefixe(a.Sad))
        else:
            return ([])
    
    def ParcoursInfixe(self,arbre):
        if arbre != None:
            return (self.ParcoursPrefixe(arbre.Sag)+ [arbre.racine.clef]+ self.ParcoursPrefixe(arbre.Sad))
        else:
            return ([])
    
    def ParcoursSuffixe(self,arbre):
        if arbre != None:
            return (self.ParcoursPrefixe(arbre.Sag)+ self.ParcoursPrefixe(arbre.Sad)+[arbre.racine.clef])
        else:
            return ([])

arb= Arbre('A')
arb.Sag=Arbre('B')
arb.Sag.Sag=Arbre('C')
arb.Sag.Sad=Arbre('D')
arb.Sag.Sad.Sag=Arbre('E')
arb.Sag.Sad.Sad=Arbre('F')
arb.Sad=Arbre('G')
arb.Sad.Sad=Arbre('H')
arb.Sad.Sad.Sag=Arbre('I')

print("####")
print(arb.GetTaille())
print("####")



print(arb.BFS())
print('####')

print(arb.ParcoursPrefixe())
print(arb.ParcoursInfixe(arb))
print(arb.ParcoursSuffixe(arb))
