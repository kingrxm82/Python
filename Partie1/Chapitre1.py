"Enregistrez des groupes de données avec les listes"

#Créer la liste
plateformes_sociales=["Facebook","Instagram","Twiitter","Tiktok"]

#Accéder aux élements de la listes 
"Accéder au premier élement de la liste"
plateformes_sociales[0]
"Accéder au dérnier élement de la liste"
plateformes_sociales[-1]

#Modifier les elements de la liste
"Au départ notre troisieme element Twitter est ecrite avec deux ii donc oa suprimer un i"
plateformes_sociales[2]="Twitter"

#Ajouter,retirer et trier des listes
"Ajout un element dans une liste"
plateformes_sociales.append("Reddit")
"Supprrimer un element dans une liste"
plateformes_sociales.remove("Reddit")
"Avoir le longueur de la liste"
len(plateformes_sociales)
"Trier la liste (Le tri se fait alphabétiquement pour les chaînes, et numériquement pour les nombres)"
plateformes_sociales.sort()

#Il existe d'autres fonctions pour y'appliquer sur les listes
"Ajouter plusieurs éléments à la fin de la liste"
plusieurs_elements = ["Snapchat","Whatsapp","Telegram"] 
plateformes_sociales.extend(plusieurs_elements)

"Insérer un élement à une position donnée dans la liste"
plateformes_sociales.insert(1,"Messenger")

"Supprimer un element dans la liste par sa posiion ou bien index"
plateformes_sociales.pop(-1) 

"Renvoyer la premiere occurence de l'element"
plateformes_sociales.index("Facebook") 

"Renvoyer la nombre d'occurence de l'element"
plateformes_sociales.count("Facebook") 

"Inverser l'ordre des élements de la liste"
plateformes_sociales.reverse()

#Trouver un élement
"Retourne True s'il existe et retourne False s'il n'existe pas"
a_trouver = "Facebok"
a_trouver in plateformes_sociales

#Les tupules
"Les tuples sont immutables (objet ne peut pas etre modifier apres sa création)"
plateformes_sociales=("Facebook","Instagram","Twiitter","Tiktok")

#Réference
"Partie 1"
"https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python/7290436-enregistrez-des-groupes-de-donnees-avec-les-listes"