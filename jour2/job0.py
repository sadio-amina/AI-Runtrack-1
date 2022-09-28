#Déclaration de la classse Personne
class Personne :
    def __init__(self, nom, prenom):       
        self.nom = nom
        self.prenom = prenom
        
    def SePresenter(self):
        #Ceci est une méthode qui affiche les nom et prénom des personnes              
        print(self.nom, self.prenom)

    def getName(self):                   # accesseurs qui permet de lire, accéder aux attributs
        return self.nom
    
    def getPrenom(self):
        return self.prenom

    def setNom(self, nv_nom):           #setteur, permet de modifier la valeur de l'attribut nom
        self.nom = nv_nom
        return nv_nom

    def setPrenom(self, nv_prenom):
        self.prenom= nv_prenom
        return nv_prenom
        
# création d'objets à partir de la classe Personne

personne1= Personne("Diop", "Abdallah")
personne2= Personne("Mendy", "  Jean")
personne3= Personne("Chidid", "Viviane")
personne4= Personne("Ronaldo", "Chris")

personne1.SePresenter() 
personne2.SePresenter()
personne3.SePresenter()
personne4.SePresenter()
