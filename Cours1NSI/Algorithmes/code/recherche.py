def recherche_element(tab,x):
    """ Fonction qui recherche si un élément est dans un tableau
    entrées : tab un tableau d'entiers et x l'entier à rechercher
    sortie : un booléen"""
    i = 0
    n = len(tab)
    while i < n and tab[i] != x:
        i = i + 1
    if i < n :
        return True
    else:
        return False

#l'élément est présent une fois
assert recherche_element([1,5,-6,12,4,7],4) == True
#l'élément est présent plusieurs fois
assert recherche_element([1,5,-6,12,1,7],1) == True
#l'élément n'est pas présent
assert recherche_element([1,5,-6,12,4,7],3) == False
#la liste est vide
assert recherche_element([],15) == False
