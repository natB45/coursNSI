import tkinter
import random

def mouve():
    """Lancer la balle"""
    global dx, dy, continuer
    if fond.coords(balle)[0] < 0 or fond.coords(balle)[0] > 670:
        dx = -dx
    if fond.coords(balle)[1] < 0 or fond.coords(balle)[1] > 430:
        dy = -dy
    fond.move(balle, dx, dy)
    if continuer:
        fenetre.after(15, mouve)


#problème on ne peut repartir
def arret():
    """Arreter la balle"""
    global continuer
    continuer = False



def quitter():
    """Fermer la fenêtre"""
    fenetre.destroy()

#création de la fenêtre
fenetre = tkinter.Tk()
fenetre.title("Introduction")
fenetre.geometry("700x500")

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

#création de la balle
x = 50
y = 50
balle = fond.create_oval(x, y, x + 30, y + 30, width = 2, fill = "#66FF99")

#accéleration
continuer = True
dx = 2
dy = 4
fenetre.mainloop()