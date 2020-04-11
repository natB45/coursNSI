#Creation de deux listes
liste1 = ["sookie","Dusty","Twist","Daisy"]
liste2 = liste1
print("L1 =",liste1)
print("L2 =",liste2)

#On modifie la liste1
liste1[0] = "Jenny"
print("L1 =",liste1)

#La liste2 a ete modifiee
print("L2 =",liste2)

#############################
### Solutions ###
#############################

#On copie liste1, en la placant a une autre adresse memoire
liste2 = liste1[:]
print("L1 =",liste1)
print("L2 =",liste2)

#On modifie la liste1
liste1[0]="Babar"
print("L1 =",liste1)
print("L2 =",liste2)  #La liste2 est inchangee


### Autre methode ###
liste3 = list(liste1)
print("L1 =",liste1)
print("L3 =",liste3)

#On modifie la liste1
liste1[0]="toto"
print("L1 =",liste1)
print("L3 =",liste3)