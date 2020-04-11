def double_boucle(liste1, liste2):
    resultat = []
    for e1 in liste1:
        valeur = 0
        for e2 in liste2:
            if e1 == e2:
                valeur += 1
        resultat.append(valeur)
    return resultat
