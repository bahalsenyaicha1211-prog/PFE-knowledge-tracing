#NOMBRE DE BONNE REPONSES
def reponses(nombres):
  if len(nombres)==0:
    return None
  liste_reponse= []

  for nombre in nombres:
      if nombre!=0 or nombre!=1:
           continue
           liste_reponse.append(nombre)
  return liste_reponse

print(reponses([0,2,4,10,11,1,]))
