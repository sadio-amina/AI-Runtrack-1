
liste_entiers=[]

for nb_entier in range (1,6):
    #nb_entier= int(input("Entrez un nombre entier : "))
    liste_entiers.append(nb_entier)
    liste_entiers= sorted(liste_entiers, reverse=False)
   

print("Les entiers saisis triés par ordre croissant: ", liste_entiers)