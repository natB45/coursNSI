#Une balle se déplace dans la fenètre en rebondissant sur les murs
import tkinter
import time
import random

def mouve(objet,x1,y1):
    deltax = 4         #décalage sur l'axe des abscisses
    deltay = 6
    while continuer:
        if x1 > 750 or x1 < 0:
            deltax = -deltax
        if y1 > 650 or y1 < 0:
            deltay = -deltay
        time.sleep(0.03)   #On met le programme en pause 0,02 secondes pour avoir le temps de visualiser le déplacement
        x1 = x1 + deltax   #on modifie l'abscisse du rond
        y1 = y1 + deltay
        can.coords(objet,x1,y1,x1+50,y1+50)

        can.update()      #on met à jour l'affichage

#Mise en place de la fenètre
fenetre = tkinter.Tk()
fenetre.title("Balle Jaune")
fenetre.geometry("800x700")

#On pose un caneva sur la fenetre, pour dessiner dessus
can = tkinter.Canvas(fenetre, width = 800, height = 800, bg = "SteelBlue1")
can.place(x = -2, y = 0)

#on trace un cercle
rond = can.create_oval(500, 150, 550, 200, width = 3, outline = "DarkOrange4", fill = "DarkOrange1")


continuer = True

#on déclenche le lancement de la balle
mouve(rond,0, 200)

fenetre.mainloop()