"Regroupez des tâches en utilisant des fonctions"

"Les fonctions sont des blocs de code réutilisables qui permettent d'organiser et de structurer le code, ainsi que de faciliter sa maintenance."

#Utilisez une fonction sans paramètres
"Créer la fonction"
def afficher_message():
    print("Bonjour, comment ca va ?")
"Appeler la fonction"
afficher_message()

#Utilisez une fonction avec paramètres
def afficher_nom_prenom(nom,prenom):
    print("Nom : ",nom)
    print("Prénom : ",prenom)
afficher_nom_prenom("Mejri","Ramzi")

# Utilisez une fonction avec une valeur de retour
def calculer_somme(a,b):
    resultat = a+b
    return resultat
somme = calculer_somme(2,10)
print(somme)

#Réference
"Partie 2"
"https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python/7296396-regroupez-des-taches-en-utilisant-des-fonctions"