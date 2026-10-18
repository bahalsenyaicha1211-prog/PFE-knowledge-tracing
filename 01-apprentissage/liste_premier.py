
from nbr_premier import est_premier #fonction qui vérifie si un nombre est premier
def list_nombres_premiers(n):
   list_premiers= []   #liste qui contiendra les nombres premiers de 2 à n

   for i in range(2,n+1):  # on parcourt tous les nombres de 2 à n
        if est_premier(i):
            list_premiers.append(i)
   return list_premiers
