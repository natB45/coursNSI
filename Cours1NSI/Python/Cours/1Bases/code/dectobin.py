def dectobin(a):
    """Permet de donner l'écriture binaire
     d'un entier naturel a
     entrée : a en base 10
     sortie : a en base 2"""
    binaire = ""
    while a != 0:    #Tant que le quotient de la division n'est pas nul
       binaire = str(a%2) + binaire    #on ajoute le reste à l'écriture binaire
       a = a//2      #on recommence avec le quotient obtenu
    return int(binaire)  #on transforme la chaine en entier

#on teste la fonction avec des résultats connus
assert dectobin(1) == 1
assert dectobin(57) == 111001
