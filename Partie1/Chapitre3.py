"Contrôlez le déroulement de votre programme avec des conditions"

#Définissez des conditions avec les instructions if/else
"IF/ELSE"
ensoleille = True
if ensoleille:
    print("On va à la plage")
else:
    print("On reste à la maison")
    
#Définissez des conditions alternatives en ajoutant une clause elif    
"IF/ELIF/ELSE"
ensoleille=False
neige=True
if ensoleille:
    print("On va à la plage")
elif neige:
    print("On fait un bonhome de neige")
else:
    print("On reste à la maison")

#Définissez des conditions multiples avec des opérateurs logiques
"IF(AND/OR/NOT)"
avec_soleil=True
en_semaine=False
if avec_soleil and en_semaine:
    print("On va au travail")
elif avec_soleil and not en_semaine:
    print("On va à la plage")
else:
    print("On reste à la maison")

#Définissez des conditions complexes avec des expressions comparatives
"IF(==/!=/</<=/>/>=)"
nombre_invites = 25
nombre_siege = 50
if nombre_invites < nombre_siege:
    print("Il reste encore de place")
else:
    print("Il n'existe plus de place")

#Réference
"Partie 2"
"https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python/7168878-controlez-le-deroulement-de-votre-programme-avec-des-conditions"