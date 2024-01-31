"Utilisez les hiérarchies d’héritage et l’héritage multiple"

#Créez des hiérarchies d’héritage
class Cat:
    def meow(self):
        print("Meow!")

class Talker:
    def say(self, to_say):
        print(to_say)

"Héritage multiple"
class TalkingCat(Cat, Talker):
    pass

"Instancnier de la classe"
salem = TalkingCat()
salem.meow()
salem.say("Hello!")

#Réferences
'Partie 2'
"https://openclassrooms.com/fr/courses/7150616-apprenez-la-programmation-orientee-objet-avec-python/7196419-utilisez-les-hierarchies-d-heritage-et-l-heritage-multiple"