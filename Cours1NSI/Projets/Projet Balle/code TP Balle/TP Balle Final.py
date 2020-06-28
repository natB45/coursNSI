import tkinter
import time
import random

def mouve():
    """Lancer la balle"""
    global continuer,x ,y, deltax, deltay
    continuer = True
    while continuer:
        if (x + deltax < 0) or (x + deltax > 670):
            collision_mur(1)
        if (y + deltay < 0) or (y + deltay) > 430:
            collision_mur(2)
        x += deltax
        y += deltay
        fond.coords(balle, x, y, x + 30, y + 30)
        fond.update()

def collision_mur(axe):
    """Changements de direction et de couleur de la balle à chaque collision avec un mur"""
    global deltax, deltay
    if axe == 1:
        deltax = - deltax
    elif axe == 2:
        deltay = - deltay
    couleur()

def couleur():
    """Changer la couleur de la balle à chaque rebond"""
    global balle
    liste_couleurs =["#3333FF", "#FF9966", "#FFFF00", "#339900", "#660033",
                     "#00FF33", "#660099", "#33CCFF"]
    n = random.randint(0,7)
    fond.itemconfig(balle, fill = liste_couleurs[n])


def arret():
    """Arreter la balle"""
    global continuer
    continuer = False
    pass

def quitter():
    """Fermer la fenêtre"""
    fenetre.destroy()

fenetre = tkinter.Tk()              #crée la fenêtre graphique
fenetre.title("Introduction")       #on peut lui donner un titre
fenetre.geometry("700x500")         #on redimensionne la fenêtre (pixels)

#Texte de présentation
affiche = tkinter.Label(fenetre,text="Lancez la balle !",font = ("Franklin Gothic Heavy", 15), fg = "DodgerBlue2")
affiche.place(x = 18, y = 458)

#Les boutons de commande
demarrer = tkinter.Button(fenetre,text="Go !", command = mouve, font = ("Franklin Gothic Heavy", 10), fg = "orange2")
demarrer.place(x = 240, y = 457)
arreter = tkinter.Button(fenetre,text="Stop", command = arret, font = ("Franklin Gothic Heavy", 10), fg = "orange2")
arreter.place(x = 300, y = 457)
quitter = tkinter.Button(fenetre,text="Fermer", command = quitter, font = ("Mistral", 14))
quitter.place(x = 625, y = 451)

#Mise en place du canevas
fond = tkinter.Canvas(fenetre, width = 700, height = 450)
fond.place(x = -2, y = -1)

#image de fond
fic_voie_lactee = tkinter.PhotoImage(file = "Images/milkywayf.png")
voie_lactee = fond.create_image(350, 225, image = fic_voie_lactee)

#accélération initiale
deltax = 0.05
deltay = 0.07

#création de la balle
x = 50
y = 50
balle = fond.create_oval(x, y, x + 30, y + 30, width = 2, fill = "#66FF99")



fenetre.mainloop()