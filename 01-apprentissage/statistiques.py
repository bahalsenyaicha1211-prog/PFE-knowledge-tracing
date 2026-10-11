#TP4 Statistique sur des notes
print("\n==================Statistique sur les notes================== ")
notes=[]        # on initialise une liste vide pour stocker les notes saisies par l'utilisateur
somme= 0.0
arret='stop'    # on définit une variable pour arrêter la saisie des notes
start = True    # on initialise une variable pour contrôler la boucle while
while start:    # on entre dans une boucle while qui continue tant que start est vrai
    note = input("Entrez une notes : ")  # on demande à l'utilisateur de saisir une note
    if note == arret:                   # si l'utilisateur saisit "stop", on arrête la saisie des notes
        start = False                   # on affiche un message pour indiquer la fin de la saisie des notes
        print("================Fin du saisis, vous trouverez ci-dessous vos statistiques================")

    else:   
        note=float(note)                # on convertit la note saisie en float et on l'ajoute à la liste des notes
        notes.append(note)              
print("Vous avez saisies {} notes".format(len(notes)))
if len(notes)>0:                        # on vérifie si la liste des notes n'est pas vide avant de calculer les statistiques
    minimum =notes[0]                   # on initialise la variable minimum avec la première note de la liste
    maximum = notes[0]                  # on initialise la variable maximum avec la première note de la liste
    for i in notes:                     # on parcourt toutes les notes de la liste pour calculer la somme, le minimum et le maximum
        if i> maximum:                  # on met à jour la variable maximum si la note courante est supérieure à la valeur actuelle de maximum
            maximum = i
        elif i<minimum:                 # on met à jour la variable minimum si la note courante est inférieure à la valeur actuelle de minimum
            minimum = i
        somme +=i                       # on calcule la somme de toutes les notes pour pouvoir calculer la moyenne

    moyenne = somme / len(notes)        # on calcule la moyenne en divisant la somme des notes par le nombre de notes saisies
    print(f"Moyenne: {moyenne} ")
    print(f"Note maximum: {maximum}")
    print(f"Note minimum: {minimum}")
else:
  print("Aucune donnée statistique")

