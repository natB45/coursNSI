def dectobin(a):
    """Permet de donner l'ecriture binaire d'un entier naturel a
     entree : a en base 10
     sortie : a en base 2"""
    binaire = ""
    while a != 0:   #Tq le quotient de la div n'est pas nul
       binaire = str(a%2) + binaire     #on ajoute le reste
       a = a//2      #on recommence avec le quotient obtenu
    return int(binaire)  #on transforme la chaine en entier

#on teste la fonction avec des resultats connus
assert dectobin(1) == 1
assert dectobin(57) == 111001
 