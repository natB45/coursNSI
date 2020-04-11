import csv


#Liste de listes d'enregistrements
def charger_liste(nom_fic):
    """
    Permet de charger un fichier CSV
    paramètre : nom_fic une chaine de caractères contenant le nom du fichier csv
    résultat : la liste des enregistrements dans le fichier (une liste de listes)
    """
    liste_enreg = []
    with open (nom_fic, "r", newline="", encoding = "utf-8") as csvfile :
    # création du lecteur csv
        fich_reader = csv.reader(csvfile, delimiter = ",")
        for enreg in fich_reader :
            #enreg est de type list
            #Le premier étant l'entête sous forme d'une liste
            liste_enreg.append(enreg)
    return liste_enreg


#Liste de dictionnaires : ici tous les champs sont conservés
def charger_liste_dico(nom_fic):
    """
    Permet de charger un fichier CSV
    paramètre : nom_fic une chaine de caractères contenant le nom du fichier csv, sans son extension
    résultat : la liste de tous les enregistrements du fichier (une liste de dictionnaires)
    """
    table = []
    # ouverture du fichier CSV
    with open(nom_fic+".csv","r", newline="", encoding = "utf-8") as csvfile :
        # création du lecteur csv indiquant le caractère séparateur
        # la ligne d'entête est utilisée pour créer les clés des dicitonnaires
        element_reader = csv.DictReader(csvfile, delimiter = ",")
        for enreg in element_reader :
        # enreg est une liste de str contenant chaque champ de l'enregistrement
        # ajout de l'enregistrement dans la liste sous forme d'un dictionnaire
            table.append(dict(enreg))
    return table

#Liste de dictionnaires : ici on choisit de ne garder que certains champs
def charger_liste_dico2(nom_fic):
    """
    Permet de charger un fichier CSV
    paramètre : nom_fic une chaine de caractères contenant le nom du fichier csv, sans son extension
    résultat : la liste d'une partie des enregistrements du fichier (une liste de dictionnaires)
    """
    super_heros = []
    # ouverture du fichier CSV
    with open(nom_fic+".csv","r", newline="", encoding = "utf-8") as csvfile :
        # création du lecteur csv indiquant le caractère séparateur
        persos_reader = csv.reader(csvfile, delimiter = ",")
        # permet de sauter la ligne d'entête si on n'en a pas besoin
        persos_reader.__next__ ()
        for enreg in persos_reader : # boucle de parcours des enregistrements
            #on indique les éléments de l'enregistrement que l'on souhaite garder
            super_heros.append({"Nom" : enreg [1], "Surnom" : enreg[2], "Année Apparition" : enreg[7]})
    return super_heros

