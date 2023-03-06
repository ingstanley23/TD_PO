

from classes.etudiant import*
#creer liste etudiant
#afficher liste etudiant

# etud1 = Etudiant()
# etud1.nom = "Morand"
# etud1.prenom = "Honiel"
# etud1.no_dossier = "01003"

# etud2 = Etudiant()
# etud2.nom = "Graville"
# etud2.prenom = "Stanley"
# etud2.no_dossier = "01005"

# etud4 = Etudiant()
# etud4.nom = "Sainterlin"
# etud4.prenom = "Edson"
# etud4.no_dossier = "01004"

etud1 = Etudiant("Morand", "Honiel", "01003")
etud2 = Etudiant("Graville", "Stanley", "01005")
etud4 = Etudiant("Edson", "Sainterlin", "01004")

etud1.presenter()


etudiants = []
etudiants.append(etud1)
etudiants.append(etud2)
etudiants.append(etud4)

for etud in etudiants:
    etud.presenter()