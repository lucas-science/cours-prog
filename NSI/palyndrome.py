def est_palindrome(mot):
    mot=mot.lower()
    for i in range(len(mot)//2):
        if mot[i]!=mot[-i-1]:
            return False
    return True


print(est_palindrome("kaak"))

def est_palindrome_recursive(mot,res=False):
    l = len(mot)
    if res == True:
        return False
    elif l < 2:
        return True
    else:
        return est_palindrome_recursive(mot[1:-1],mot[0] != mot[-1])


print(est_palindrome_recursive("s a u a s"))

