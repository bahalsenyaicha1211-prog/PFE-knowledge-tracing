#NOMBRE DE BONNE REPONSES
# fonction qui prend en entrée une liste de nombres et retourne une liste contenant uniquement les nombres 0 et 1
def reponses(nombres):

  liste_reponse= []

  for nombre in nombres: # Filtrer les nombres pour ne garder que 0 et 1
      if nombre==0 or nombre==1:
          liste_reponse.append(nombre)
  return liste_reponse     #retourner la liste des réponses filtrées

# fonction qui calcule le taux de réussite à partir d'une liste de réponses (0 et 1)
def taux_de_reussite(liste):
    compteur = 0
    for i in liste:  # compter le nombre de réponses correctes (1) dans la liste
        if i == 1:
            compteur +=i
    if compteur == 0:
        return 0.0
    else:
        return compteur/len(liste) # retourner le taux de réussite en divisant le nombre de réponses correctes par la taille de la liste
# fonction qui calcule le taux de réussite sur les k dernières réponses d'une liste
def reussite_recente(liste, k):
   if k <= 0:
      return taux_de_reussite(reponses((liste))) #retourner le taux de réussite sur toutes les réponses si k est inférieur ou égal à 0

   return taux_de_reussite(reponses(liste[-k:]))     # retourner le taux de réussite sur les k dernières réponses

# fonction qui calcule la plus longue série de réponses correctes (1) dans une liste
def plus_longue_serie(liste):
  serie_en_cours = 0
  meilleur_serie = 0

  for  element in reponses(liste):  # parcourir la liste des réponses filtrées pour ne garder que 0 et 1
      if element == 1:
        serie_en_cours += 1
      else:
        serie_en_cour = 0
      if  serie_en_cours > meilleur_serie: # mettre à jour la meilleure série si la série en cours est plus longue
          meilleur_serie = serie_en_cours
  return meilleur_serie