"Utilisez des objets dans des collections"

#Utiliser des onjets dans une collection
class Person:
    def __init__(self,name):
        self.name=name
    def walk(self):
        print(f"{self.name} marche")

volunteers = [Person("Ramzi"),Person("Intissar")]
for volunteer in volunteers:
    volunteer.walk()

#Réferences
"Partie 2"
"https://openclassrooms.com/fr/courses/7150616-apprenez-la-programmation-orientee-objet-avec-python/7196587-utilisez-des-objets-dans-des-collections"