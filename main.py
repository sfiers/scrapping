from bs4 import BeautifulSoup

f = open("recette.html", "r")
html_content = f.read()
f.close()



soup = BeautifulSoup(html_content, "html.parser")

titre_h1 = soup.find("h1")
text_titre = titre_h1.text

liste_div_centre = soup.find_all("div", class_="centre")

paragraphe_description = liste_div_centre[1].find("p", class_="description")
text_description = paragraphe_description.text

div_info = soup.find('div', class_="info")
img_info = div_info.find("img")


print ("Titre de la page:", text_titre)
print ("La description:", text_description)
print ("La src de l'img:", img_info["src"])