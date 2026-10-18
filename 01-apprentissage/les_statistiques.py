# fonctions pour calculer les statistiques sur une liste de notes
def minimum(notes):
    if len(notes) == 0:
        return None
    plus_petit = notes[0] # on initialise la variable plus_petit avec la première note de la liste
    for i in notes:
        if i < plus_petit:
            plus_petit = i
    return plus_petit
# fonctions pour calculer les statistiques sur une liste de notes
def maximum(notes):
    if len(notes) == 0:
        return None
    plus_grand = notes[0] # on initialise la variable plus_grand avec la première note de la liste
    for i in notes:
        if i > plus_grand:
            plus_grand = i
    return plus_grand

# fonctions pour calculer les statistiques sur une liste de notes
def moyenne_notes(notes):
    somme = 0.0
    compteur = 0
    for i in notes:
        if i < 0:
            continue
        somme += i
        compteur +=1
    if compteur == 0:
        return None   # on retourne None si la liste est vide ou si toutes les notes sont négatives
    else:
        return somme / compteur
