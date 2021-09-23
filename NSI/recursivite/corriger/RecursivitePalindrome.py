# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 19:36:05 2021

@author: mfb
"""

# Résolution de la symétrie d'une chaîne de caractères

def FindPalindrome( mot):
    mot = mot.lower()
    for i in range(len(mot)//2):
        if(mot[i] != mot[-1-i]):
            return(False)
    return(True)
    
    
def RecurFindPalindrome(mot):
    if(len(mot) < 2):
        return True
    else:
        print(mot)
        print(mot[0] == mot[-1])
        return ( RecurFindPalindrome(mot[1:-1]) and (mot[0] == mot[-1]) )

Phrase = str(input("Saisir la chaîne de caractères : "))
Phrase = Phrase.replace(" ","")                             # Supprime les espaces de la chaîne de caractères
Phrase = Phrase.lower()                                     # Passage en minuscule de tous les caractères
print(Phrase)
print("la chaîne de caractère : '",Phrase, end ="'")
print()


#if(FindPalindrome(Phrase) == True):
if(RecurFindPalindrome(Phrase) == True):
    print("est un palindrome.")
else:
    
    print("n'est pas un palindrome.")
    
    