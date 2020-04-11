#1 : Création d'un dictionnaire avec pour clées le nom des produits
#et pour valeurs la quantité disponible
petit_dej = {"Lait":4,"Biscottes":10,"Céréales":8,"jus_orange":5,"Beurre":3}

#2
def affiche_produits(stock):
    """Fonction qui affiche les produits du dictionnaire donné en
    paramètre et qui représente le stock."""
    return list(stock.keys())

#3
def quantite_produit(stock,produit):
    """Fonction qui retourne la quantité du produit dans le stock.
    On donne les stock disponible sour forme d'un dictionnaire,
    et le produit recherché sous forme d'une chaine de caractères."""
    return stock[produit]

#4
def modifier_stock(stock,nom_prod,modif_quantite):
    """Fonction qui modifie la quantité disponible d'un produit dans le
    stock;
    paramètres d'entrée : le stock (dictionnaire);
    le nom du produit dont la quantité doit être modifiée (chaine
    de caractères), la quantité à ajouter ou enlever (un entier avec
    un signé).
    Elle retourne le nouveau stock."""
    if modif_quantite < 0 and stock[nom_prod] + modif_quantite < 0:
        print("Une telle quantité du produit ",nom_prod," n'est pas disponible !")
    else:
        stock[nom_prod] = stock[nom_prod] + modif_quantite
        return stock

#5
def ajouter_produit(stock,new_prod,quantite_new_prod):
    """Fonction qui ajoute un produit au stock ;
    on entre le stock sous forme d'un dictionnaire,
    le nouveau produit à ajouter (une chaine de caractères)
    et sa quantité (un entier naturel).
    Elle retourne le stock modifié (dictionnaire)."""
    stock[new_prod] = quantite_new_prod
    return stock