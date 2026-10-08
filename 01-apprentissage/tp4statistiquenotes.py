#TP4 Statistique sur des notes
print("\n==================Statistique sur les notes================== ")
notes=[]
somme= 0.0
arret='stop'
start = True
while start:
    note = input("Entrez une notes : ")
    if note == arret:
        start = False
        print("================Fin du saisis, vous trouverez ci-dessous vos statistiques================")
       
    else:
        note=float(note)
        notes.append(note)
if len(notes)>0:
    minimum = notes[0]
    maximum = notes[0]      
    for i in notes:
        if i> maximum:
            maximum = i
        elif i<minimum:
            minimum = i
        somme +=i
       
    moyenne = somme / len(notes)
    print(f"Moyenne: {moyenne} ")
    print(f"Note maximum: {maximum}")
    print(f"Note minimum: {minimum}")
    
        
