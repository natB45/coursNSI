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

assert nbre_occurences("","r") == ("r",0)
assert nbre_occurences("ananas","a") == ("a",3)
assert nbre_occurences("chat","z") == ("z",0)
assert nbre_occurences("feu","u") == ("u",1)
assert nbre_occurences("bicyclette","T") == ("T",0)