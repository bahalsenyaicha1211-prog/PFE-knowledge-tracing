from les_statistiques import moyenne_notes #importation de la fonction moyenne_notes depuis le module les_statistiques
# fonction qui calcule la moyenne des notes pour chaque étudiant dans un dictionnaire de notes
def moyenne_par_etudiant(dictionnaire_notes):
    relutat = {}
    for etudiant, notes in dictionnaire_notes.items():  # on parcourt chaque étudiant et ses notes dans le dictionnaire
        moyenne = moyenne_notes(notes)
        relutat[etudiant] = moyenne  # on stocke la moyenne calculée pour chaque étudiant dans le dictionnaire relutat
    return relutat

# fonction qui détermine l'étudiant ayant la meilleure moyenne parmi un dictionnaire d'étudiants et de leurs moyennes
def  meilleur_etudiant(etudiants):
    meilleur = None
    meilleure_moyenne = -1
    for etudiant, moyenne in etudiants.items():
        if moyenne is not None and moyenne > meilleure_moyenne:
            meilleure_moyenne = moyenne
            meilleur = etudiant
    return meilleur, meilleure_moyenne

etudiants = {"Amal": [12, 15, 14], "Karim": [8, 10, 9], "Sara": [16, 18]}  # on définit un dictionnaire d'étudiants avec leurs notes respectives
print(moyenne_par_etudiant(etudiants))
print(meilleur_etudiant(moyenne_par_etudiant(etudiants))) # on affiche le dictionnaire des moyennes par étudiant et l'étudiant ayant la meilleure moyenne