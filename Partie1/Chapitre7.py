"Extrayez et transformez des données avec l’extraction web"

#Le package Requests / Le package Beautiful Soup
import requests
from bs4 import BeautifulSoup

url = "https://www.gov.uk/search/news-and-communications"

"Récuperer le code HTML du site"
page=requests.get(url)

"Parser le HTML avec les attributs HTML"
soup=BeautifulSoup(page.content,'html.parser')

"Recupérer les titres dans le site web"
titres = soup.find_all("a",class_="govuk-link")

"Recupérer les descriptions dans le site web"
descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")

"Initialiser les deux listes"
liste_titres = []
liste_descriptions = []

"Transformer les donnees dans des listes"
for titre in titres:
    liste_titres.append(titre.string)
    
for desctiption in descriptions:
    liste_descriptions.append(desctiption.string)

#Réferences
"Partie 3"
"https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python/7296776-extrayez-et-transformez-des-donnees-avec-lextraction-web"