from bs4 import BeautifulSoup

f = open("recette.html", "r")
html_content = f.read()
f.close()



soup = BeautifulSoup(html_content, "html.parser")

titre_h1 = soup.find("h1")
text_titre = titre_h1.text

print ("Titre de la page:", text_titre)