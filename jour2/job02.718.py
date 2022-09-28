class Personne :
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def sePresenter(self):
        print(self.nom, self.prenom)

    def getNom(self):
        return self.nom

    def getPrenom (self) :
        return self.prenom

class Livre :
    def __init__(self, titre) :
        self.titre = titre
        self.oeuvres = []


    def getTitre(self):
        return self.titre

    def Print(self):
        print ("Le titre du livre : ", self.titre) 

    
    def getOeuvre (self):
        return self.oeuvres

    def listerOeuvre(self):
        for livre in self.getOeuvre():
            print(livre.getTitre())

class Client (Personne) :
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)

class Bibliotheque :
    def __init__(self, nom, titre, catalogue): 
        self.nom = nom
        self.catalogue = {}
        self.oeuvres =[]

    
    def getOeuvre (self):
        return self.oeuvres

    def listerOeuvre(self):
        for livre in self.getOeuvre():
            print(livre.getTitre())
    def acheterLivre :
        def __init__(self, auteur, titre, n):
            pass



