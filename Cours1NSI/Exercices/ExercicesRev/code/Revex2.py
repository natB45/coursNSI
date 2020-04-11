def inconnue(liste1,liste2):
    nouvelle_liste = []
    for i in range(len(liste1)):
        if liste1[i] < liste2[i]:
            nouvelle_liste.append(liste1[i])
        elif liste1[i] > liste2[i]:
            nouvelle_liste.append(liste2[i])
    return nouvelle_liste