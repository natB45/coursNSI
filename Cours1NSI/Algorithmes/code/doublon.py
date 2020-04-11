import time
import numpy as np
import matplotlib.pyplot as plt
import random

def recherche_doublon(table):
    for i in range(len(table)):
        for j in range(i+1,len(table)):
            if table[i] == table[j]:
                return True
    return False

def generation_tableau(n):
    table = []
    for i in range(n):
        table.append(random.randint(1,100))
    return table


taille = int(input("Quelle taille devra avoir votre liste ?"))
x = np.array([i for i in range(taille)])
y = np.array(generation_tableau(taille))
plt.plot(x, y)

plt.show()