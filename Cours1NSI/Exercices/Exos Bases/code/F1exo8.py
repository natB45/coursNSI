def kchiffres(nombre,k):
    """on affiche les k derniers chiffres de nombre, en commençant par l'unité,
    nombre est un entier positif et k est un entier strictement positif"""
    nombre = str(nombre)    #on transforme nombre en chaine de caractère pour accéder à chaque chiffre
    n = len(nombre)
    new = ""
    if k <= n:         #si k ne dépasse pas le nombre de chiffres
        for i in range(k):
            new = new + nombre[n-1-i]
        return int(new)   #on transforme la chaine en entier
    else:
        for i in range(n):
            new = new + nombre[n-1-i]  #on inverse les chiffres
        return int(new + "0"*(k-n))         #on ajoute des zéros pour avoir k chiffres