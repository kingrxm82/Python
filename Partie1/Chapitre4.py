"Répétez des tâches facilement à l’aide de boucles"

#Utilisez la boucle for
"FOR ... IN ..."
races_de_chien = ["golden retriever", "chihuahua", "terrier", "carlin"]
for chien in races_de_chien:
    print(chien)

#Utilisez la boucle while
"WHILE ... OPERATION"
capacite_maximale = 10
capacite_actuelle = 3 
while capacite_actuelle < capacite_maximale:
    capacite_actuelle+=1

#Utilisez les mot-clés break  et continue
"BREAK"
"L'instruction break  permet de sortir d'une boucle prématurément. Elle est souvent utilisée lorsqu'une condition est rencontrée, et que l'on souhaite arrêter la boucle avant qu'elle ne se termine normalemen"
for i in range(10):
    if i == 5:
        break
    print(i)
"CONTINUE"
"L'instruction  continue  permet de passer à la prochaine itération de la boucle, sans exécuter le reste du code présent dans la boucle pour l'itération en cours"
liste=[1,2,3,4,5]
for i in liste:
    if i == 3:
        continue
    print(i)

#Réference
"Partie 2"
"https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python/7296286-repetez-des-taches-facilement-a-laide-de-boucles"