def inverser(chaine):
    """paramètre : une chaine de caractères
    sortie : la chaine avec les caractères dans l'ordre inverse"""
    new_chaine = ""
    n = len(chaine)                #on regarde la longueur de la chaine
    for i in range(n):             #on parcourt la chaine
        new_chaine = new_chaine + chaine[n-i-1] #on part de la fin de la chaine
    return new_chaine
    
