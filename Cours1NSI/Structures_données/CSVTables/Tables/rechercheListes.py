import csv

def charger_liste(nom_fic):
    """
    Permet de charger un fichier CSV
    paramètre : nom_fic une chaine de caractères contenant le nom du fichier csv
    résultat : la liste des enregistrements dans le fichier (une liste de listes)
    """
    liste_enreg = []
    with open (nom_fic, "r", newline="", encoding = "utf-8") as csvfile :
    # création du lecteur csv
        fich_reader = csv.reader(csvfile, delimiter = ";")
        for enreg in fich_reader :
            #enreg est de type list
            #Le premier étant l'entête sous forme d'une liste
            liste_enreg.append(enreg)
    return liste_enreg

jo = charger_liste("JO_Liste_Medaille_2012-2014.csv")

def appartient(nom,table):
    for ligne in table:
        if ligne[3] == nom:
            return True
    return False

appartient("LAVILLENIE",jo)
appartient("NAT",jo)

def nombre_medailles(athlete,table):
    """Donne le nombre de médailles obtenues par l'athlète
    paramètres : athlete, une chaine de caractère correspondant au nom de l'athlète
    et table, la liste des médaillés aux JO
    résultat : un entier égal au nombre de médailles obtenues par l'athlète"""
    nombre_medailles = 0
    for ligne in table:
        if ligne[3] == athlete:
            nombre_medailles += 1
    return nombre_medailles

nombre_medailles("LAVILLENIE",jo)
nombre_medailles("LE FUR",jo)

def select(table):
    new_liste = []
    for ligne in table:
        if ligne[6] == "Or":
            new_liste.append(ligne)
    return new_liste

select(jo)

def select(table):
    new_liste = []
    for ligne in table:
        if ligne[5] == "F" and ligne[6] == "Argent":
            new_liste.append(ligne)
    return new_liste

select(jo)

def trier_liste(table):
    return sorted(table, key=lambda ligne: ligne[3])

trier_liste(jo)

def trier_liste2(table):
    return sorted(table, key=lambda ligne: ligne[4])
trier_liste(jo)

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

heros = charger_liste_dico("superHeros")

def extraire(table):
    new_heros =[]
    for dico in table:
        new_heros.append({"Nom" : dico["Nom"], "Pseudo" : dico["Pseudo"]})
    return new_heros

extraire(heros)

def extraire2(table,liste_cles):
    new_heros =[]
    for dico in table:
        new_dico = {cle : dico[cle] for cle in dico if cle in liste_cles}
        new_heros.append(new_dico)
    return new_heros

extraire2(heros,["Nom","Année_apparition"])

heroines = charger_liste_dico("superHeroines")

def fusion_listes_memes_champs(tab1,tab2):
    """Fusion de tables identiques
    paramètres : les deux tables à fusionner (liste de dictionnaires)
    sortie : nouvelle liste constitué des deux autres"""
    return tab1+tab2

fusion_listes_memes_champs(heros,heroines)



liste_eleves = [{"nom" : "Dupond", "prénom" : "Jacques", "age" : 16},
                {"nom" : "Bourgeois", "prénom" : "Nicolas", "age" : 16},
                {"nom" : "Etoile", "prénom" : "Caroline", "age" : 17},
                {"nom" : "Trunc", "prénom" : "Jessie", "age" : 15},
                {"nom" : "Kennedy", "prénom" : "Maelle", "age" : 16}]
liste_notes = [{"nom" : "Dupond", "prénom" : "Jacques", "maths" : 12, "français" : 9},
                {"nom" : "Bourgeois", "prénom" : "Nicolas",  "maths" : 19, "français" : 7},
                {"nom" : "Etoile", "prénom" : "Caroline", "maths" : 12, "français" : 9},
                {"nom" : "Trunc", "prénom" : "Jessie", "maths" : 5, "français" : 12},
                {"nom" : "Kennedy", "prénom" : "Maelle",  "maths" : 10, "français" : 17}]

def creation_fusion(enreg1,enreg2):
    """Fonction créant un dictionnaire eleve avec tous les champs de la fusion
    paramètres : enreg1 et enreg2 sont des éléments des deux tables à fusionner ;
    sortie : on retourne le dictionnaire complet représentant l'élève."""
    return {"nom" : enreg1["nom"], "prénom" : enreg1["prénom"], "age" : enreg1["age"],
            "maths" : enreg2["maths"], "Français" : enreg2["français"]}

def fusion(tab1,tab2):
    tableau_complet = []
    for dico1 in tab1:
        for dico2 in tab2:
            if dico1["nom"] == dico2["nom"]:
                tableau_complet.append(creation_fusion(dico1,dico2))
    return tableau_complet

fusion(liste_eleves,liste_notes)

##########
def recherche_doublons(tab):
    """Rechercher d'éventuels doublons et les supprimer
    paramètre : tab, une liste de dictionnaires
    sortie : une liste sans doublons"""
    for i in range(len(tab)):
        present = False
        for j in range(i+1,len(tab)):
            if tab[i]["nom"] == tab[j]["nom"]:
                present = True
        if present == True:
            tab.remove(tab[i])
    return tab

liste=[{"nom":"bubulle","categorie":"élève","age":15},{"nom":"nat","categorie":"alien","age":18},
       {"nom":"bubulle","categorie":"élève","age":15},{"nom":"nat","categorie":"alien","age":18},
       {"nom":"nat","categorie":"vivante","age":18},{"nom":"toto","categorie":"singe","age":25}]

liste_essai = list(liste) #on copie la liste dans une nouvelle liste pour la modifier

recherche_doublons(liste_essai)

