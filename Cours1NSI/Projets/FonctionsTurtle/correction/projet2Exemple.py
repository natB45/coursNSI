"""Ce programme affiche une fenêtre ou se dessinent des étoiles et des carrés,
   de tailles aléatoire et positionnés au hasard.

   Usage:
   ======
   python projet2.py nb_elements

   nb_elements : le nombre d'éléments à représenter.
"""
__author__ = ("Nathalie Bessonnet")
__date__ = "18/11/2019"

#on importe le module Turtle
import turtle
#on importe la fonction randint du module random
import random


#Fonction qui trace un carré
def carre(c,x,y):
    """cette fonction trace un carré de côté c, dont le coin
    inférieur gauche a pour coordonnées (x,y)"""
    turtle.color("black")
    turtle.width(2)
    turtle.fillcolor((0.85,0.5,0.98)) #Couleur de remplissage en RGB
    turtle.begin_fill()               #Commencer à remplir
    turtle.up()                       #Lever le crayon
    turtle.goto(x,y)                  #Se placer aux coordonnées demandées
    turtle.down()                     #Poser le crayon
    for i in range(4):                #Tracer les côtés du carré
        turtle.forward(c)             #Avancer de la longueur du côté
        turtle.left(90)               #Tourner à gauche à angle droit
    turtle.end_fill()                 #Arrêter le remplissage

#Fonction qui trace une étoile à 6 branches
def etoile(t,x,y):
    turtle.color("black")
    turtle.width(1)
    turtle.fillcolor((0.98,0.9,0.5))
    turtle.begin_fill()
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    for i in range(12):                  #On répète le tracé d'une branche
        turtle.forward(t)
        turtle.right(150)
    turtle.end_fill()


#Création d'une liste aléatoire de 0 et de 1, de taille n
def liste_aleatoire(n):
    liste =[]
    for i in range(n):
        liste.append(random.randint(0,1))
    return liste


#Ici commence le programme principal
if __name__ == "__main__":
    #On demande le nombre d'éléments à tracer
    nb_elements = eval(input("Combien d'éléments voulez-vous dessiner ?"))
    #Création d'une liste de 0 et de 1
    liste_choisie = liste_aleatoire(nb_elements)
    turtle.speed(10)                     #Vitesse maximale pour le tracé
    for element in liste_choisie:        #On parcoure la liste
        #on choisit la taille des éléments au hasard
        taille = random.randint(15,80)
        #On choisit au hasard les coordonnées pour placer l'élément
        posx = random.randint(-380,380)
        posy = random.randint(-380,380)
        if element == 0:                #Si 0 on trace un carré
            carre(taille,posx,posy)
        else:                           #Sinon on trace une étoile
            etoile(taille,posx,posy)
    turtle.ht()                         #Faire disparaitre la tortue
    turtle.exitonclick()                #Fermer la fenêtre si on clique dessus

