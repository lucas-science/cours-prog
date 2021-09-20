def est_palindrome(mot):
    mot=mot.lower()
    for i in range(len(mot)//2):
        if mot[i]!=mot[-i-1]:
            return False
    return True


print(est_palindrome("kaak"))

def est_palindrome_recursive(mot,res=False,i=0):
    l = len(mot)//2
    if res == True:
        return False
    elif i == l:
        return True
    else:
        return est_palindrome_recursive(mot,mot[i] != mot[-i-1],i+1)


print(est_palindrome_recursive("raddar"))
"""

si i == 0
retourner res

sinon 
retourner 

"""
