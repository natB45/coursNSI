def division(a,b):
    """La fonction doit renvoyer la quotient et le reste de
    la division euclidienne de a par b ;
    a et b sont des entiers positifs, avec b non nul"""
    r = a
    q = 0
    while r >= b:
        q +=1
        r = r - b
    return (q,r)

assert division(15,3) == (5,0)  #le reste est nul
assert division(25,4) == (6,1)  #le reste est non nul
assert division(8,1) == (8,0)   #on divise par 1
assert division(4,10) == (0,4)  #a est inférieur à b