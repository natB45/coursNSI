def tri_selection(tab):
    for i in range(len(tab)-1):
        min = tab[i]
        indice_min = i
        for j in range(i+1,len(tab)):
            if tab[j] < min:
                min = tab[j]
                indice_min = j
        tab[i], tab[indice_min] = min, tab[i]
    return tab


def tri_selection_bis(tab):
    for i in range(len(tab)-1):
        indice_min = i
        for j in range(i+1,len(tab)):
            if tab[j] < tab[indice_min]:
                indice_min = j
        tab[i], tab[indice_min] = tab[indice_min], tab[i]
    return tab