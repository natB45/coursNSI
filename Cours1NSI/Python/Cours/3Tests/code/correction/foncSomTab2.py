def somme_liste(tab):
    """Cette fonction renvoie la somme des termes d'une
    liste, non vide, de nombres donnée en entrée"""
    assert len(tab) > 0, "La liste est vide !"
    s = 0
    for i in range(len(tab)):
        s += tab[i]
    return s


assert somme_liste([1]) == 1
assert somme_liste([3,0,-4,11]) == 10
assert somme_liste([-5,2,0.5]) == -2.5

