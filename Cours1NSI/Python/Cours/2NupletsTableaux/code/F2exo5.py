def paireImpaire(nuplet):
    """Fonction qui prend un tuple comportant des entiers positifs en parametre
       et renvoie deux listes (dans un tuple), l'une avec les nombres pairs
       et l'autre avec les nombres impairs.
    """
    #Creation des listes paires et impaires.
    liste_pairs = []
    liste_impairs = []
    #On parcoure du tuple donne.
    for nombre in nuplet:
        if nombre%2 == 0:                #Si le nombre est pair
            liste_pairs.append(nombre)   #On l'ajoute a la liste paire
        else:
            liste_impairs.append(nombre)
    return liste_pairs,liste_impairs