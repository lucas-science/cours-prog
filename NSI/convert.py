
def DecToBase(n,b):
    assert (b==2 or b == 8 or b== 16) , " Uniquement avec une des bases usuelles "
    symboles = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    res = ""
    while (n!=0):
        res = symboles[n%b] + res
        n = n//b
    return res



#print(DecToBase(76,2))

def DecToBase_recurs(n,b,res):
    symboles = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    if n == 0:
        return res
    else:
        return DecToBase_recurs(n//b,b,symboles[n%b] + res)


#print(DecToBase_recurs(76,2,""))




def bTodec(mot,b):
    signes=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    result=0
    p=len(mot)
    for i in range(p):
        result=result + signes.index(mot[i]) * b**(p-i-1)
    return result
    
#print(bTodec("01011001",2))
#print(bTodec("F5",16))

def bTodec_recurs(mot,b,res=0,n=0):
    signes=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    if n == len(mot):
        return res
    else:
        #print(n,mot[len(mot)-n-1])
        return bTodec_recurs(mot,b,res + signes.index(mot[len(mot)-1-n]) * b**n,n+1)


#print(bTodec_recurs("01011001",2))
#print(bTodec_recurs("F5",16))