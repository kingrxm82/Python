"Enregistrez des données complexes avec des dictionnaires"

"Un dictionnaire est une structure de données qui enregistre des données dans des paires clés-valeurs"

#Créer un dictionnaire
nouvelle_compagne = {
    "nom_de_compagne" : "Mario Dev",
    "responsable" : "Ramzi Mejri",
    "date_debut": "01/01/2024",
    "influenceurs_importants" : ["@intissartaboubi","@kingrxm82"]
}

#Accéder a une valeur dans un dictionnaire
nouvelle_compagne["nom_de_compagne"]
nouvelle_compagne["responsable"]

#Réaliser des opérations
"Ajouter une paire clé-valeur"
nouvelle_compagne["Lieu"] = "Chicago"

"Supprimer une paire clé-valeur"
del nouvelle_compagne["Lieu"]

#Il existe d'autres fonctions pour y'appliquer sur les dictionnaires
"Retourner tous les clés de le dictionnaire"
nouvelle_compagne.keys()

"Retourner tous les valeurs de le dictionnaire"
nouvelle_compagne.values()

"Retourner une vue sur les couples (clé, valeur) du dictionnaire"
nouvelle_compagne.items()

"Retourner la valeur spécifié au clé"
nouvelle_compagne.get("nom_de_compagne")

"Supprimer le clé et retourne le valeur specifé"
nouvelle_compagne.pop("influenceurs_importants")

"Effacer le dictionnaire"
nouvelle_compagne.clear()

#Trouver un élement
"Seulement par les clés"
"Retourne True s'il existe et retourne False s'il n'existe pas"
a_trouver="nom_de_compagne"
a_trouver in nouvelle_compagne

#Réference
"Partie 1"
"https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python/7290721-enregistrez-des-donnees-complexes-avec-des-dictionnaires"