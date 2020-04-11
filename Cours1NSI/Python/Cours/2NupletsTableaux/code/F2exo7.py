#creation d'un tableau de dimensions 4*3, avec des zeros pour elements
tableau = [[0]*3 for i in range(4)]
for i in range(4):          #On l'affiche ligne par ligne
    print(tableau[i])
print()

#On modifie le contenu du tableau
for i in range(4):             #On parcoure les lignes
    for j in range(3):         #On parcoure les colonnes
        tableau[i][j] = i*j    #On remplace les elements

#On affiche le tableau modifie
for i in range(4):
    print(tableau[i])