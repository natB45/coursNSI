#############################
#Une liste de dictionnaires
#############################
#Liste de dictionnaires représentant les clients :
clients_dico = [{"nom":"Longhorn","prenom":"Archibald","adresse":"10 rue des Murlins","ville":"Orleans"},
           {"nom":"Passoire","prenom":"Elodie","adresse":"5 allée des Pommiers","ville":"Olivet"},
           {"nom":"Batracien","prenom":"Joseph","adresse":"5 bis rue du Terroir","ville":"Saint-Jean Le Blanc"}]

def ville_client(nom_client):
    """On obtient la ville de résidence d'un client ;
    entrée : le nom du client (str)
    sortie : le nom de la ville où il habite (str)
    """
    for i in range(len(clients_dico)):
        if clients_dico[i]["nom"] == nom_client:
            return clients_dico[i]["ville"]

#Les données de M. Batracien
assert clients_dico[2] == {"nom":"Batracien","prenom":"Joseph","adresse":"5 bis rue du Terroir","ville":"Saint-Jean Le Blanc"}
#La ville où réside Mme Passoire
assert clients_dico[1]["ville"] == "Olivet"

def ajout(nom_cli,prenom_cli,adresse_cli,ville_cli):
    """Cette fonction ajoute un client à la liste ;
    entrées : on donne le nom, le prénom, l'adresse, puis la ville du nouveau
    client (str)
    sortie :la liste des clients à laquelle on a ajouté le nouveau client.
    """
    new_client = {"nom" : nom_cli, "prenom" : prenom_cli, "adresse" : adresse_cli, "ville" : ville_cli}
    clients_dico.append(new_client)
    return clients_dico

#Tests de la fonction ville-client
assert ville_client("Passoire") == "Olivet"
assert ville_client("Quiça") == None

#############################
#Une liste de listes
#############################
#Liste de listes représentant les clients :
clients_liste = [["Longhorn","Archibald","10 rue des Murlins","Orleans"],
           ["Passoire","Elodie","5 allée des Pommiers","Olivet"],
           ["Batracien","Joseph","5 bis rue du Terroir","Saint-Jean Le Blanc"]]

#Les données de M. Batracien
assert clients_liste[2] == ["Batracien","Joseph","5 bis rue du Terroir","Saint-Jean Le Blanc"]
#La ville où réside Mme Passoire
assert clients_liste[1][3] == "Olivet"

def ville_client2(nom_client):
    """On obtient la ville de résidence d'un client ;
    entrée : le nom du client (str)
    sortie : le nom de la ville où il habite (str)
    """
    for i in range(len(clients_liste)):
        if clients_liste[i][0] == nom_client:
            return clients_liste[i][3]

#Tests de la fonction ville-client
assert ville_client2("Passoire") == "Olivet"
assert ville_client2("Quiça") == None

def ajout2(nom_cli,prenom_cli,adresse_cli,ville_cli):
    """Cette fonction ajoute un client à la liste ;
    entrées : on donne le nom, le prénom, l'adresse, puis la ville du nouveau
    client (str)
    sortie :la liste des clients à laquelle on a ajouté le nouveau client.
    """
    clients_liste.append([ nom_cli, prenom_cli, adresse_cli, ville_cli])
    return clients_liste

