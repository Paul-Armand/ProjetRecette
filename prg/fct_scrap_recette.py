import requests
from bs4 import BeautifulSoup

def retour_liste_recette(nom_recette):
    lower_nom_recette = nom_recette.lower()
    nom_recette_adapte = '-'.join(lower_nom_recette.split(" "))
    url_recettes = f"https://www.marmiton.org/recettes/recherche.aspx?aqt={nom_recette_adapte}"
    rep_recettes = requests.get(url_recettes)

    soup = BeautifulSoup(rep_recettes.text, "html.parser")
    liste_a = soup.find_all("a", class_="MRTN__sc-1gofnyi-2 gACiYG")

    liste_liens = []
    for recette in liste_a:
        liste_liens.append(recette['href'])
    return liste_liens

def retour_liste_ingredients(liste_liens, numero_recette):
    lien_recette = liste_liens[numero_recette-1]
    url_recette = f"https://www.marmiton.org{lien_recette}"
    rep_recette = requests.get(url_recette)

    soup = BeautifulSoup(rep_recette.text, "html.parser")

    liste_span = soup.find_all("span", class_="SHRD__sc-10plygc-0 kWuxfa")
    liste_elements = []
    for span in liste_span:
        liste_elements.append(span.text)

    liste_span = soup.find_all("span", class_="SHRD__sc-10plygc-0 epviYI")
    liste_quantite = []
    for span in liste_span:
        liste_quantite.append(span.text)

    liste_ingredients = []
    for iteration in range(len(liste_elements)):
        element = liste_elements[iteration]
        quantite = liste_quantite[iteration]
        ingredient = f"{quantite} {element}"
        liste_ingredients.append(ingredient)
    return liste_ingredients

if __name__ == '__main__':
    nom_recette = input("Quelle recette souhaitez-vous?")
    liste_liens = retour_liste_recette(nom_recette)
    for index,lien in enumerate(liste_liens):
        texte = 'recette_'
        debut = lien.find(texte)
        fin = lien.find('.aspx')
        print(f"{index+1} : {lien[debut+len(texte):fin]}")

    numero_recette = int(input("Quel numéro de recette souhaitez-vous?"))
    liste_ingredients = retour_liste_ingredients(liste_liens, numero_recette)
    print(liste_ingredients)