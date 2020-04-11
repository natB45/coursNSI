def tri_insertion(tab):
    for i in range(1,len(tab)): #on décale les indices car le premier indice est 0
        e = tab[i]
        k = i-1
        while k >= 0 and tab[k] > e:  #là aussi !
            tab[k+1] = tab[k]
            k = k-1
        tab[k+1] = e
    return tab
