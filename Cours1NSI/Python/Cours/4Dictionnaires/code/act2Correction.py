#Création d'un nouveau fichier
with open('fichier1.txt','w') as mon_fichier:
    mon_fichier.write("Hello !")

with open('fichier1.txt','a') as mon_fichier: #Ajout d'une ligne dans le fichier
    mon_fichier.write("\nJe m'appelle Nat.")  #Sauter à la ligne suivante

#Lecture globale du fichier
with open('fichier1.txt','r') as mon_fichier:
    chaine = mon_fichier.read()

#Lecture du fichier ligne par ligne
with open("fichier1.txt", "r") as mon_fichier:
    ligne = mon_fichier.readline()  #On récupère une ligne du fichier
    while ligne != "":              #Tant que la ligne n'est pas vide
        print(ligne,end="")                #On affiche la ligne
        ligne = mon_fichier.readline()

#On récupère les lignes du fichier dans une liste
with open('fichier1.txt','r') as mon_fichier:
    liste1 = mon_fichier.readlines()

#On récupère ajoute les lignes du fichier dans une liste, en supprimer les sauts
liste2 = []
with open('fichier1.txt','r') as mon_fichier:
    for ligne in mon_fichier:
        liste2.append(ligne.rstrip('\n\r'))
