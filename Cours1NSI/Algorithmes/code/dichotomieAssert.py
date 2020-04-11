def recherche_dichotomique(tab,e):
    a = 0
    b = len(tab) - 1
    while b-a >= 0:
        milieu = (a+b)//2  #obtenir un entier
        if tab[milieu] == e:
            return True
        elif tab[milieu] > e:
            b = milieu - 1
        else:
            a = milieu + 1
    return False

assert recherche_dichotomique([],1) == False
assert recherche_dichotomique([2,5,6,15,17,18,25],6) == True
assert recherche_dichotomique([2,5,6,18,15,17,18,25],2) == True
assert recherche_dichotomique([2,5,6,18,15,17,18,25],1) == False
