class Etudiant:
    nom = ""
    prenom = ""
    no_dossier = ""
    
    def __init__(self, nom, prenom, no_dossier):
        self.nom = nom
        self.prenom = prenom
        self.no_dossier = no_dossier
        
    def __str__(self):
        return "[{self.nom} {self.prenom} {self.no_dossier}]".format(self = self)
    
    def getNomComplet(self):
        return self.nom + " " + self.prenom
    
    def presenter(self):
        print("Nom: ", self.nom)
        print("Prenom: ", self.prenom)
        print("no_dossier: ", self.no_dossier)
        print("___________________\n")
        