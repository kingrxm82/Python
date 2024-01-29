"Chargez des données avec Python"

#Creer un fichier
# fichier=open("test.csv","w")
# fichier.close()

#Le Package csv
import csv
import requests
from bs4 import BeautifulSoup

#Liser les fichier externes
with open ("Chapitre8.csv")as fichier:
    "La méthode reader va prendre tout le texte dans un CSV, le parser ligne par ligne et convertir chaque ligne dans une liste de chaînes"
    reader=csv.reader(fichier,delimiter=',')
    for ligne in reader:
        print(ligne)
    "DictReader cette méthode sait que la première ligne est un en-tête, et sauvegarde les autres lignes en tant que dictionnaires. Chaque clé est un nom de colonne, et la valeur est la valeur de la colonne."
    reader=csv.DictReader(fichier,delimiter=',')
    for ligne in reader:
        print(ligne["nom"] +" travaille comme "+ ligne["metier"]+" et son couleur préferé est le "+ ligne["couleur_preferee"])
        
"Extrait de codes de chapitre 7"
url = "https://www.gov.uk/search/news-and-communications"
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
titres = soup.find_all("a",class_="govuk-link")
descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")
liste_titres = []
liste_descriptions = []
for titre in titres:
    liste_titres.append(titre.string)
for desctiption in descriptions:
    liste_descriptions.append(desctiption.string)

#Ecrivez dans des fichiers externes
en_tete=["titre","description"]
with open ("data.csv",'w')as fichier:
    "Creer un object d'ecriture avec ce fichier"
    writer=csv.writer(fichier,delimiter=',')
    writer.writerow(en_tete)
    for titre,description in zip(liste_titres,liste_descriptions):
        ligne=[titre,description]
        writer.writerow(ligne)

#Réferences
"Partie 3"
"https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python/7300396-chargez-des-donnees-avec-python"