import string

class Alphabet_majuscules():    #classe mère
    def __init__(self):
        self.lettres = string.ascii_uppercase	# Récupère toutes les lettres de l'alphabet en Majuscule

class Alphabet_minuscules(Alphabet_majuscules):     #classe fille de Aphabet majuscules
    def __init__(self):
        Alphabet_majuscules.__init__(self)      #on récupère les majuscules
        self.lettres = self.lettres.lower ()    #on les mets en minucules

class Alphabet_tri (Alphabet_minuscules): # classe fille de minuscules donc petite-fille de majuscules
    def __init__(self):
        Alphabet_minuscules.__init__(self)  #on récupère les les minuscules
        self.voyelles = []    #on créé la méthode voyelles
        self.consonnes = []  #on créé la méthode consonnes
        for lettre in self.lettres :
            if lettre in "aeiouy":
                self.voyelles.append (lettre)  #on ajoute les voyelles
            else :
                self.consonnes.append (lettre)  #on ajoute les consonnes
    def listes_vers_chaines (self) :
        self.voyelles_chaine = "".join (self.voyelles)  #on créé une chaine avec la liste de voyelles
        self.consonnes_chaine = "".join (self.consonnes)  #on crée une chaine avec la liste des consonnes

maj = Alphabet_majuscules()
print(maj.lettres)

min = Alphabet_minuscules()
print(min.lettres)

test = Alphabet_tri()
test.listes_vers_chaines()
print(test.consonnes_chaine)