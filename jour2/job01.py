class Personne : 
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def Presentation(self):
        print(self.nom, self.prenom)

    def getNom(self):
       return self.nom

    def getPrenom(self):
        return self.prenom


class Auteur (Personne):
    def __init__(self, nom, prenom, oeuvre):
        super().__init__(nom, prenom)
        self.oeuvre = []
       
        self.oeuvre.append(livre1)
        self.oeuvre.append(livre2)
        self.oeuvre.append(livre3)

    def listerOeuvre(self):
        for livre in self.oeuvre:
            livre.Print()

    def ecrireUnLivre(self, titre):
        nv_livre = livre4.titre
        self.oeuvre.append(nv_livre)
        print(nv_livre)

class Livre (Auteur):
    def __init__(self,titre):
        self.titre = titre
        
    def Print(self):
        print("Le titre du livre est : ", self.titre)


#Création d'instances


livre1 = Livre("sous lorage")
livre2 = Livre("une si longue lettre")
livre3 = Livre("l'alchimie")
livre4 = Livre("jadore")
a= Auteur ("sadio","amina",[])

#Appel des méthodes
a.listerOeuvre()
a.Presentation()
a.ecrireUnLivre("Devenir")


    










