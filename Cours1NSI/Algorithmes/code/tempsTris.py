import time  #Module permettant de mesurer le temps d'exécution de la fonction
import random #pour créer un tableau de nombres choisis au hasard

def tri_selection(tab):
    for i in range(len(tab)-1):
        min = tab[i]
        indice_min = i
        for j in range(i+1,len(tab)):
            if tab[j] < min:
                min = tab[j]
                indice_min = j
        tab[i], tab[indice_min] = min, tab[i]
    return tab

def tri_insertion(tab):
    for i in range(1,len(tab)):
        e = tab[i]
        k = i-1
        while k >= 0 and tab[k] > e:
            tab[k+1] = tab[k]
            k = k-1
        tab[k+1] = e
    return tab

def generateur_tableau(n):
    tab =[]
    for i in range(n):
        tab.append(random.randint(1,100))
    return tab

taille = int(input("Donner la taille du tableau à trier : "))

tableau = generateur_tableau(taille)

depart = time.perf_counter()   #on note l'heure avant l'exécution
tri_selection(tableau)
temps = time.perf_counter() - depart  #on récupère l'heure après l'excution
                                      #à laquelle on enlève l'heure de départ
print("pour taille=", taille, " le temps d'exécution du tri par selection = ", temps)

depart = time.perf_counter()   #on note l'heure avant l'exécution
tri_insertion(tableau)
temps = time.perf_counter() - depart
print("pour taille=", taille, " le temps d'exécution du tri par insertion = ", temps)

depart = time.perf_counter()   #on note l'heure avant l'exécution
sorted(tableau)
temps = time.perf_counter() - depart
print("pour taille=", taille, " le temps d'exécution du tri Python (sorted) = ", temps)