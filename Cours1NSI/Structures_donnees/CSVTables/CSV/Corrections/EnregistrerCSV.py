import csv

def sauver_donnees(nom_fic, tab, entetes):
    """
    Permet de sauvegarder une liste de listes dans un fichier CSV
    paramètres :
    nom_fic : nom du fichier csv que l'on va créer, sous la forme "nom.csv"
    tab : liste de listes
    entetes est une liste de noms pour les champs du fichier
    resultat : aucun
    """
    # ouverture du fichier CSV en mode écriture
    with open(nom_fic, "w", newline ="", encoding = "utf-8") as csvfile:
        # création du lecteur csv indiquant le caractère séparateur
        liste_writer = csv.writer(csvfile, delimiter = ";")
        # permet d'écrire la ligne d'entête
        liste_writer.writerow(entetes)
        for ligne in tab : # boucle de parcours de la liste
            # ligne est une liste du tableau
            liste_writer.writerow([ligne[i] for i in range(len(ligne))])
    return None

animaux = [["chien","Dusty",1],["chienne","Sookie",2],["Chat","Twist",3],["Chatte","Daysie",1.5]]

#sauver_donnees("anim.csv",animaux,["Race","Nom","age"])

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

notes = [{"nom" : "nat","maths" : 14,"phys" : 19,"anglais" : 9}, {"nom" : "john","maths" : 18,"phys" : 13,"anglais" : 12}, {"nom" : "lili","maths" : 8,"phys" : 10,"anglais" : 15}]

#sauver_donnees2("MesNotes.csv", notes)

################################################################################
#Autres versions
################################################################################

def sauver_donnees3(nom_fic, tab):
    """
    Permet de sauvegarder une liste dans un fichier CSV
    paramètres :
    nom_fic : nom du fichier csv que l'on va créer, sous la forme "nom.csv"
    tab : liste de dictionnaires comportant 2 clés
    cle1 et cle2 sont des chaînes de caractères correspondant aux clés des dictionnaires
    resultat : aucun
    """
    # ouverture du fichier CSV en mode écriture
    with open(nom_fic, "w", newline ="", encoding = "utf-8") as csvfile:
        # création du lecteur csv indiquant le caractère séparateur
        liste_writer = csv.writer(csvfile, delimiter = ";")
        #liste des clés du dictionnaire
        entete = list(tab[0].keys())
        # permet d'écrire la ligne d'entête avec les clés pour nom de champs
        liste_writer.writerow(entete)
        for dico in tab : # boucle de parcours de la liste
            # dico est un dictionnaire du tableau
            liste_writer.writerow([dico[entete[i]] for i in range(len(dico))])
    return None

def sauver_donnees4(nom_fic, tab, entete1, entete2):
    """
    Permet de sauvegarder une liste dans un fichier CSV
    paramètres :
    nom_fic : nom du fichier csv que l'on va créer, sous la forme "nom.csv"
    tab : liste de listes de longueur 2
    entete1 et entete2 sont des chaînes de caractères décrivant les champs des
    listes
    resultat : aucun
    """
    # ouverture du fichier CSV en mode écriture
    with open(nom_fic, "w", newline ="", encoding = "utf-8") as csvfile:
        # création du lecteur csv indiquant le caractère séparateur
        liste_writer = csv.writer(csvfile, delimiter = ";")
        # permet d'écrire la ligne d'entête
        liste_writer.writerow([entete1, entete2])
        for ligne in tab : # boucle de parcours de la liste
            # ligne est une liste du tableau
            liste_writer.writerow([ligne[0], ligne[1]])
    return None

#liste_writer.writerow([dico[entete[0]], dico[entete[1]],dico[entete[2]],dico[entete[3]]])

