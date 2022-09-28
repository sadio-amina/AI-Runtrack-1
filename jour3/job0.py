chaine_de_caractere = input("Renseignez une chaine de caractère : ")
fichier = open("output.txt", "w")
fichier.write(chaine_de_caractere)
fichier.close()