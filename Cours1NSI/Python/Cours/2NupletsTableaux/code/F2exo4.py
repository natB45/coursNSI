def multiples(n):
    """Fonction qui prend en parametre un entier naturel n non nul,
       et renvoie la liste des dix premiers multiples non nuls de n
    """
    liste_multiples = []
    for i in range(1,11):
        liste_multiples.append(n*i)
    return liste_multiples