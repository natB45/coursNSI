from random import choice

liste_mots = []
with open('mots.txt','r') as mon_fichier:
    for mot in mon_fichier:
        liste_mots.append(mot.rstrip('\n\r'))

#Question 1
print("Il y a ",len(liste_mots)," mots dans le fichier.")
print("Voici un mot choisi au hasard dans la liste :",choice(liste_mots))

#Question 2
def plus_long(liste):
    """on retourne le mot le plus long, ainsi que sa taille (tuple),
    d'une liste de mots donnée en paramètre"""
    mot_le_plus_long = ""
    for element in liste:
        if len(element) > len(mot_le_plus_long):
            mot_le_plus_long = element
    return mot_le_plus_long,len(mot_le_plus_long)


