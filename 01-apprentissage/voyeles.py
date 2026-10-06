def getvoyelles_number(mot):
    compteur = 0
    voyelles = []
    mot_miniscule = mot.lower()
    liste_voyelles = ['a','e','u','i','o','y']
    for  i in mot_miniscule:
        if i in liste_voyelles:
            compteur +=1
            voyelles.append(i)
    return compteur,voyelles

x = input("Ecrivez un mot:  ")
nombre_voyelles,voyelle_trouvee = getvoyelles_number(x)
print("ce  mot contient {} voyelles {} ".format(nombre_voyelles,voyelle_trouvee))
