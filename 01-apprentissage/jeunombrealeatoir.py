from random import randint 

nombre_aleatoire =randint(1,100)

print("\n=========Bienvenu dans ce jeu de devinette, vous devinez le nombre generer par l'ordidinateur========= \n=========Ce nombre est comprit entre 1 à 100.=========")
jeu = True
compteur = 0
while jeu:
    compteur +=1
    choix = int(input("Trouvez le nombre : \n << "))
    if choix < nombre_aleatoire:
        print("Le nombre est plus grand que votre choix.")
        
    elif choix > nombre_aleatoire:
        print("Le nombre est plus petit que votre choix.")

    else:
        print("Bravo vous avez trouvé le nombre. après {} essais.".format(compteur))
        jeu = False
  
print("Fin du jeu.")
