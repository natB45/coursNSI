def indice_max_tableau(tab):
    """Cette fonction donne l'indice du
     maximum de la liste tab ;
     on suppose la liste tab non vide."""
    if len(tab) == 0:
        return None
    else:
        indice_max = 0
        for i in range(len(tab)):
            if tab[i] > tab[indice_max]:
                indice_max = i
        return indice_max

assert indice_max_tableau([]) == None
assert indice_max_tableau([-5]) == 0
assert indice_max_tableau([10,20,-30]) == 1
assert indice_max_tableau([7,-3,5,-2,7]) == 0

