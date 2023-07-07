import fct_scrap_recette

nom_recette = input("Quelle recette souhaitez-vous?")
liste_liens = fct_scrap_recette.retour_liste_recette(nom_recette)
for index,lien in enumerate(liste_liens):
    texte = 'recette_'
    debut = lien.find(texte)
    fin = lien.find('.aspx')
    print(f"{index+1} : {lien[debut+len(texte):fin]}")

numero_recette = int(input("Quel numéro de recette souhaitez-vous?"))
liste_ingredients = fct_scrap_recette.retour_liste_ingredients(liste_liens, numero_recette)
print(liste_ingredients)