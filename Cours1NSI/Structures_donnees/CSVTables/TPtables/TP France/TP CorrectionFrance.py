import csv

#question a)
def charger_liste_dico(nom_fic):
    """
    Permet de charger un fichier CSV
    paramètre : nom_fic une chaine de caractères contenant le nom du fichier csv, sans son extension
    résultat : la liste de tous les enregistrements du fichier (une liste de dictionnaires)
    """
    table = []
    # ouverture du fichier CSV
    with open(nom_fic,"r", newline="", encoding = "utf-8") as csvfile :
        # création du lecteur csv indiquant le caractère séparateur
        # la ligne d'entête est utilisée pour créer les clés des dicitonnaires
        element_reader = csv.DictReader(csvfile, delimiter = ";")
        for enreg in element_reader :
        # enreg est une liste de str contenant chaque champ de l'enregistrement
        # ajout de l'enregistrement dans la liste sous forme d'un dictionnaire
            table.append(dict(enreg))
    return table

#question b)
prenoms_France = charger_liste_dico("France-prenoms-2018.csv")

#question c)
nombre_enregistrements = len(prenoms_France)
#Il y en a 636474.

#question d)
for i in range(len(prenoms_France)):
    prenoms_France[i]["NOMBRE"] = int(prenoms_France[i]["NOMBRE"])

#question e)
def pourcentage_prenom(prenom,annee):
    """Fonction qui indique le pourcentage d'enfants ayant reçu le prenom
    indiqué l'année donnée.
    paramètres : prenom, une chaine de caractère indiquant le prénom recherché
    et annee, une chaine de caractères indiquant l'année recherchée
    sortie : un pourcentage sous forme d'entier naturel"""
    for i in range(len(prenoms_France)):
        if prenoms_France[i]["PREUSUEL"] == prenom and prenoms_France[i]["ANNAIS"] == annee:
            return prenoms_France[i]["NOMBRE"]
    return None
#LEO en 2001 soit 3


#question f)
def select(table):
    new_table = []
    for i in range(len(table)):
        if table[i]["SEXE"] == "2" and table[i]["ANNAIS"] == "2018":
            new_table.append(table[i])
    return new_table

feminin_2018 = select(prenoms_France)

#question g)
def trier_liste(table):
    return sorted(table, key=lambda ligne: ligne["NOMBRE"])

new_feminin = trier_liste(feminin_2018)
#new_feminin[-2] donne EMMA comme étant le prénom le plus répandu  en 2018.

#question h)
def sauver_donnees2(nom_fic, tab):
    """
    Permet de sauvegarder une liste de dictionnaires dans un fichier CSV
    paramètres :
    nom_fic : nom du fichier csv que l'on va créer, sous la forme "nom.csv"
    tab : liste de dictionnaires
    resultat : aucun
    """
    with open(nom_fic, "w", newline ="", encoding = "utf-8") as csvfile:
        # création du lecteur csv indiquant le caractère séparateur
        #fieldnames permet d'écrire la ligne d'entête avec les clés pour nom de champs
        liste_writer = csv.DictWriter(csvfile, fieldnames=tab[0].keys(), delimiter = ";")
        #on écrit la ligne d'entête
        liste_writer.writeheader()
        for dico in tab :
            # dico est un dictionnaire du tableau
            liste_writer.writerow(dico)
    return None

sauver_donnees2("feminin_2018.csv",feminin_2018)