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
        element_reader = csv.DictReader(csvfile, delimiter = ",")
        for enreg in element_reader :
        # enreg est une liste de str contenant chaque champ de l'enregistrement
        # ajout de l'enregistrement dans la liste sous forme d'un dictionnaire
            table.append(dict(enreg))
    return table

#question b)
prenoms_USA = charger_liste_dico("USA-prenoms-1880-2008.csv")

#question c)
nombre_enregistrements = len(prenoms_USA)
#Il y en a 258000.

#question d)
for i in range(len(prenoms_USA)):
    prenoms_USA[i]["POURCENTAGE"] = float(prenoms_USA[i]["POURCENTAGE"])

#question e)
def pourcentage_prenom(prenom,annee):
    """Fonction qui indique le pourcentage d'enfants ayant reçu le prenom
    indiqué l'année donnée.
    paramètres : prenom, une chaine de caractère indiquant le prénom recherché
    et annee, une chaine de caractères indiquant l'année recherchée
    sortie : un pourcentage sous forme d'entier naturel"""
    for i in range(len(prenoms_USA)):
        if prenoms_USA[i]["NOM"] == prenom and prenoms_USA[i]["ANNEE"] == annee:
            return prenoms_USA[i]["POURCENTAGE"]
    return None
#James en 1913 soit 0.038851%

#question f)
def select(table):
    new_table = []
    for i in range(len(table)):
        if table[i]["SEXE"] == "girl" and table[i]["ANNEE"] == "2000":
            new_table.append(table[i])
    return new_table

feminin_2000 = select(prenoms_USA)

#question g)
def trier_liste(table):
    return sorted(table, key=lambda ligne: ligne["POURCENTAGE"])

new_feminin = trier_liste(feminin_2000)
#new_feminin[-1] donne Emily comme étant le prénom le plus répandu  en 2000.

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
        liste_writer = csv.DictWriter(csvfile, fieldnames=tab[0].keys(), delimiter = ",")
        #on écrit la ligne d'entête
        liste_writer.writeheader()
        for dico in tab :
            # dico est un dictionnaire du tableau
            liste_writer.writerow(dico)
    return None

sauver_donnees2("feminin_2000.csv",feminin_2000)
