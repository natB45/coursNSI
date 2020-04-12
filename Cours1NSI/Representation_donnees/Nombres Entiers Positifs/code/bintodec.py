def bintodec(a):
    a = str(a)       #on transforme le nre en chaine de carctère
    n = len(a)       #on obtient la longueur de la chaine = nbre de bits
    decimale = 0
    for i in range(n):
        if a[n-i-1] == "1":    #si le bit est à 1, en lisant de droite à gauche
            decimale = decimale + 2**(i)  #on ajoute 2^i à la somme
    return decimale
    
assert bintodec(1110) == 14
assert bintodec(110011011) == 411