"Créez et utilisez des objets Python"

#Instancier un objet
"Créer la classe Rectangle"
class Rectangle:
    def __init__(self,width,height,color="red"):
        self.width=width
        self.height=height
        self.color=color
"On faire instance pour l'objet rectangle"
rectangle1=Rectangle(4,3)
rectangle2=Rectangle(4,3,"blue")
rectangle3=Rectangle(4,3,color="blue")

#Modifier un objet
rectangle2.width=8
rectangle3.width=12
rectangle3.color="green"

#Les differents attributs
#Attributs d'instance
"Les attributs d’instance sont des variables définies à l’aide deself. Elles sont relatives à l’instance, et ne peuvent être accédées sans instanciation. Dans le cadre des méthodes, ce sont les méthodes classiques d'une classe, qui possèdent  self  en premier paramètre."
#Attributs de classe
"Les attributs de classe sont des variables définies directement dans le corps de la classe. Elles peuvent être accédées par la classe, sans passer par l’instanciation. Les attributs de classe peuvent se référencer entre eux, mais ne peuvent pas accéder aux attributs d’instance."
"Dans le cadre des méthodes, elles seront précédées par un  @classmethod, et leur premier paramètre seracls(à la place deself)"
#Attributs statiques
" Enfin, les attributs statiques sont des attributs qui n’ont pratiquement aucun lien avec la classe. Seules les méthodes peuvent être statiques, et l’ajout par rapport aux attributs de classe est minime : on n'a plus besoin de spécifier le paramètre  cls. Pour créer un attribut statique, il suffit de faire précéder la méthode par  @staticmethod"

#Réferences
"Partie 1"
"https://openclassrooms.com/fr/courses/7150616-apprenez-la-programmation-orientee-objet-avec-python/7195794-creez-et-utilisez-des-objets-python"