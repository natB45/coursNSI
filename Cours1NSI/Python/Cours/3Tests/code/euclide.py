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
