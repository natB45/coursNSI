def nbre_occurences(mot,lettre):
    """On donne en paramètre un mot et une lettre, de types str,
    et cette fonction retourne le nombre de fois où la lettre
    apparaît dans le mot, ainsi que la lettre recherchée,
    sous forme d'un tuple."""
    compteur = 0
    for l in mot:
        if l == lettre:
            compteur = compteur +1
    return (lettre,compteur)
