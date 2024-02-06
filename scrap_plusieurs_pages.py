#exercices
""" 1)Observe attentivement l'URL de la page 1. Essaye de passer à la page 2. Dans un notebook python, essaye de générer automatiquement les URL des 5 premières pages (avec une boucle par exemple ?)

2)Utilise BeautifulSoup pour scraper les facts et les notes des 5 premières pages, grâce aux URL que tu as générées. (Nous pourrions faire les 100 ou 200 pages suivantes, mais ca risque d'entrainer une charge inutile pour ceux qui administrent ce serveur.) Le résultat doit être dans un dictionnaire.

3)Crée un DataFrame contenant ces données, il doit donc posséder 2 colonnes et 100 lignes.

4)Crée une visualisation de la distribution des notes. """

#importe bibio
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
# Visualisation
import seaborn as sns
import matplotlib.pyplot as plt
#creer boucle for d'aller page 1 au page 5
#url = "http://www.chucknorrisfacts.fr/facts/top/{page_num}"
pages=[]

for i in range(1,6):
  url=f"http://www.chucknorrisfacts.fr/facts/top/"+str(i)
  pages.append(url)
#print(pages)
dictt={}
for item in pages:
  page = requests.get(item)
  soup = bs(page.text, 'html.parser')

  containers= soup.find_all("div",{"class":"card"})


  for container in containers:
    blaque=container.find_all("div",{"class":"card-body bg-light rounded"})
    #print(blaque[0].text.strip())
    blague = blaque[0].text.strip()
    notes=container.find("span")
    #print(notes.text.strip())
    note_val = notes.text.strip()
    dictt.setdefault(blague, note_val)
#print(dictt)
dff=pd.DataFrame(dictt.items(), columns=['blagues', 'note_val'])
#print(dff)
sns.histplot(data = dff, x = 'note_val',binwidth=0.05)
plt.title("Distribution des notes")
plt.ylabel('Nombre de blagues')
plt.xlabel('Note')
plt.xlim(8, 9)
plt.ylim(0,100)