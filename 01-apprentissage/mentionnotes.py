#TP 3: notes et mention

print("Bienvue dans l'observateur de moyenne:")
moyenne = -1                # on initialise la variable moyenne à -1 pour entrer dans la boucle while
while moyenne <0 or moyenne >20:   # on vérifie que la moyenne saisie est comprise entre 0 et 20
    print("Entrez la moyenne de l'étudiant barrièrre sur 20 : ")
    moyenne = float(input("<< "))           # on convertit la saisie en float pour pouvoir effectuer des calculs
if moyenne >=16:
    print("Mention Très bien!")             # on affiche la mention correspondante à la moyenne saisie
elif moyenne >=14:
    print("Mention Bien")
elif moyenne >=12:
    print("Mention Assez bien")
elif moyenne >=10:
    print("Mention Passable")
else:
    print("Ajournée")
