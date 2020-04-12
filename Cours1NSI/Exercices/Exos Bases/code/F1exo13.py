def miroir(chaine):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    inverse = "zyxwvutsrqponmlkjihgfedcba"
    nouvelle_chaine = ""
    for caractere in chaine:               #recherche de l'indice de la lettre
        i = 0
        while caractere != alphabet[i]:
            i += 1
        nouvelle_chaine = nouvelle_chaine + inverse[i]
    return nouvelle_chaine

print(miroir("nat"))