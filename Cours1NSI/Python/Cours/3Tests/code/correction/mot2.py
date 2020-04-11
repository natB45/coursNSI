def deb_mot_egal_fin(mot):
    """Fonction qui retourne True si la premiere lettre et la derniere lettre
    du mot sont les mêmes et False sinon ;
    la variable mot est une chaîne de caracteres"""
    if len(mot)==0:
        return None
    else:
        if mot[0].lower() == mot[len(mot)-1].lower():
            return True
        else:
            return False

assert deb_mot_egal_fin("rouler") == True   #on a la même lettre
assert deb_mot_egal_fin("chien") == False   #les lettres sont différentes
assert deb_mot_egal_fin("") == None    #le mot est vide
assert deb_mot_egal_fin("Ana") == True  #Avec une majuscule et une minuscule
assert deb_mot_egal_fin(" ici") == False  #avec un espace au début