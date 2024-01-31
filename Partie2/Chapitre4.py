"Surchargez les méthodes en Python"

"Une classe abstraite est une classe qui ne peut pas être instanciée – la seule façon de l’utiliser est de créer une sous-classe"

#Accédez aux méthodes des parents
"Créer la classe mére"
class Drink:
    def __init__(self,price):
        self.price=price
    def drink(self):
        print("Je ne sais pas ce que c'estn mais je bois")
"Créer la classe enfant"
class Coffe(Drink):
    prices = {"simple":1,"serré":2,"allongé":1.5}
    def __init__(self, type):
        self.type=type
        "On hérite l'attrbut price par la classe mere et on modifie selon notre besoin"
        super().__init__(price=self.prices.get(type,1))
        "On a accédé au methode des parents et on a la modifié"
    def drink(self):
        print("un bon café pour réveiller")
        
#Réferences
"Partie 2"
"https://openclassrooms.com/fr/courses/7150616-apprenez-la-programmation-orientee-objet-avec-python/7196334-surchargez-les-methodes-en-python"