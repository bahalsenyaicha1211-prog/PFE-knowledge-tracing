#Liste des nombre de prémier de 2 à N
nombre = int(input("Entrez un nombre entier:\n<< "))
if nombre <2:
    print("Aucun nombre premier, votre nombre doit être superieur ou egale à 2")
else:
    print("===============liste de nombre prémiers de 2 à {}===============".format(nombre))
    for i in range(2,(nombre+1)): # Parcourt tous les nombres de 2 à nombre
        est_premier = True          # on suppose que le nombre est premier
        for j in range(2,(i//2)+1): # Parcourt tous les nombres de 2 à la moitié du nombre i
            if i%j == 0:             # Si le reste de la division de i par j est égal à 0, alors i n'est pas premier
                est_premier = False
                break               # On sort de la boucle car on a trouvé un diviseur
        if est_premier:             # Si le nombre est premier, on l'affiche
            print(f"{i}")
     
    print("===============Fin du programme===============")