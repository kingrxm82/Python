"Écrivez une classe Python"

#Syntaxe de classe
"Création de classe"
class Rectangle:
    "Attributs"
    width=3
    height=2
    "Méthodes"
    def calculate_area(self):
        return self.width*self.height

#Utilisation des constructeurs
class Rectangle:
    "Autre facon pour déclarer les attributs"
    def __init__(self,width,height,color="red"):
        self.width=width
        self.height=height
        self.color=color

"Partie 1"
"https://openclassrooms.com/fr/courses/7150616-apprenez-la-programmation-orientee-objet-avec-python/7195400-ecrivez-une-classe-python"