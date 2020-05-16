import csv      #module pour travailler avec les fichiers csv

#question 1
def charger_table(nom_fichier):
    """
    Permet de charger un fichier CSV
    entrée : nom_fic une chaine de caractères contenant le nom du fichier csv
    sortie : la liste des enregistrements dans le fichier (une liste de listes)
    """
    table = []
    # ouverture du fichier CSV
    with open(nom_fichier,"r", newline="", encoding = "utf-8") as csvfile :
        # création du lecteur csv indiquant le caractère séparateur
        # la ligne d'entête est utilisée pour créer les clés des dicitonnaires
        element_reader = csv.DictReader(csvfile, delimiter = ";")
        for enreg in element_reader :
        # enreg est une liste de str contenant chaque champ de l'enregistrement
        # ajout de l'enregistrement dans la liste sous forme d'un dictionnaire
        #on transforme les valeurs numériques en entiers
            enreg["Courage"] = int(enreg["Courage"])
            enreg["Loyauté"] = int(enreg["Loyauté"])
            enreg["Sagesse"] = int(enreg["Sagesse"])
            enreg["Malice"] = int(enreg["Malice"])
            table.append(dict(enreg))
    return table

#liste de dictionnaires comportant les élèves de Poudlard
eleves_poudlard = charger_table("choixpeauMagique.csv")

#question 2
def distance(e1, e2):
    """Calcul de la distance de Manhattan avec les valeurs numériques de deux élèves
    entrées : deux dictionnaires représentant deux éleves de Poudlard
    sortie : un entier représentant la distance entre ces deux élèves
    """
    #on ne garde que les valeurs numériques (on enlève le nom et la maison, pour obtenir une liste
    liste1 = list(e1.values())[1:5]
    liste2 = list(e2.values())[1:5]
    dist = 0
    for i in range(4):
        dist = dist + abs(liste1[i] - liste2[i])
    return dist

#question 3
def proches_voisins(new_eleve, liste_eleves):
    """Fonction qui détermine les maisons des 7 plus proches voisins d'un élève parmi ceux de
    Poudlard.
    entrées : new_eleve un dictionnaire représentant le nouvel élève(sans maison) ;
     liste_eleves une liste de dictionnaires représentants les élèves de Poudlard
    sortie : liste de tuples (distance, maison) comportant les 7 élèves les plus proches du
    nouvel élève
    """
    liste_distances =[]
    #pour chaque élève de Poudlard
    for el in liste_eleves:
        #on calcule la distance
        d = distance(new_eleve, el)
        #on ajoute la distance et la maison à la liste
        liste_distances.append((d,el["Maison"]))
    #on trie la liste par ordre croissant
    liste_distances = sorted(liste_distances)
    #on ne garde que les 7 premiers résultats de la liste
    return liste_distances[0:7]

#question 4
def prediction_maison(eleve, liste_eleves):
    """Fonction qui pour un élève donné donne la maison à laquelle il devrait
    appartenir.
    entrées : eleve est un dictionnaire représentant un nouvel élève, liste_eleves
    une liste de dicitonnaire comprenant tous les élèves de l'école.
    sortie : une chaine de carctères indiquant la maison du nouevl élève
    """
    #on récupère les 7 plus proches voisins de l'élève
    plus_proches = proches_voisins(eleve,liste_eleves)
    #on crée un dictionnaire avec toutes les maisons
    maisons = {"Serpentar" : 0, "Gryffondor" : 0, "Poufsouffle" : 0, "Serdaigle" : 0}
    #on compte le nombre d'élèves dans chaque maison
    for el in plus_proches:
        maisons[el[1]] +=1
    #on détermine la maison pour laquelle la valeur est maximale
    #on initialise avec Serpentar
    max = maisons["Serpentar"]
    rep = "Serpentar"
    for nom in maisons:
        #si la maison est plus représentée, elle prend la place du max
        if maisons[nom] > max:
            max = maisons[nom]
            rep = nom
    return rep

eleve1 = {"Nom" : "Hermione", "Courage" : 8, "Loyauté" : 8, "Sagesse" : 8, "Malice" : 6}
eleve2 = {"Nom" : "Drago", "Courage" : 6, "Loyauté" : 6, "Sagesse" : 5, "Malice" : 8}
eleve3 = {"Nom" : "Cho", "Courage" : 6, "Loyauté" : 6, "Sagesse" : 9, "Malice" : 6}
eleve4 = {"Nom" : "Cédric", "Courage" : 7, "Loyauté" : 10, "Sagesse" : 5, "Malice" : 6}

