def echange(tab,i,j):
    """Fonction qui echange les termes de rang i
       et j dans la liste tab,
       et retourne la liste modifiee
    """
    tab[i],tab[j] = tab[j],tab[i]
    return tab

