class PPile():
    def __init__(self):
        self.pile = None

    def Construire(self):
        self.pile = []
        return self.pile

    def Empiler(self,x):
        self.pile.append(x)
    
    def Depiler(self):
        if len(self.pile) != 0:
            return self.pile.pop()
        else:
            print("erreur : pas d'élément à supprimer")

    def Est_vide(self):
        if self.pile == []:
            return True
        else: 
            return False

    def Obtenir_Pile(self):
        return self.pile

class FFile():
    def __init__(self) -> None:
        self.file = []

    def Defiler(self):
        if len(self.file) != 0:
            return self.file.pop(0)
        else:
            print("erreur : pas d'élément à supprimer")

    def Enfiler(self,e):
        return self.file.append(e)

    def Est_Vide(self):
        if len(self.file) == 0:
            return True
        else:
            return False

    def Obtenir_File(self):
        return self.file

ma_pile = PPile()
ma_pile.Construire()
print(ma_pile.Obtenir_Pile())

ma_pile.Empiler(3)
ma_pile.Empiler(7)
ma_pile.Empiler(6)
ma_pile.Empiler(8)

ma_pile.Depiler()
ma_pile.Depiler()

ma_pile.Empiler(5)

print(ma_pile.Obtenir_Pile())

print(ma_pile.Est_vide())