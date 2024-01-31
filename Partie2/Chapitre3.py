"Écrivez une sous-classe en Python"

#Héritage
"La classe mére"
class Film:
    def __init__(self,name):
        self.name=name
    def watch(self):
        print("Bon visionnage !")

# "La classe FilmCassete hérite la classe mére Film"
# class FilmCassette(Film):
#     pass

"On peut ajouter d'autres attributs et d'autres méthode"
class FilmCassette(Film):
    def __init__(self, name):
        self.name
        self.magnetic_tape=True
    def rewind(self):
        print("C'et long à rembobiner")
        self.magnetic_tape=True

        
#Réferences
"Partie 2"
"https://openclassrooms.com/fr/courses/7150616-apprenez-la-programmation-orientee-objet-avec-python/7196232-ecrivez-une-sous-classe-en-python"