import string

menu = ["Voir la liste de course", "Ajouter un produit", "Supprimer un produit", "Quitter"]
liste_de_course = []
def afficher_menu(liste):
    print("========== MENU ===========")
    for i in range(len(liste)) :
        print(f"{string.ascii_lowercase[i]}. {liste[i]}")
    print("===========================")

def afficher_liste_de_course(liste):
    print("----- LISTE DE COURSE -----")
    if len(liste) == 0 :
        print("Vide")
    else :
        for i in range(len(liste)) :
            print(f"{str(i+1)}. {liste[i]}")
    print("---------------------------")

def ajouter_produit(liste):
    produit = input("Quel produit voulez-vous ajouter ?")
    if produit.capitalize() in liste:
        print("Ce produit est déjà présent dans votre liste")
    else:
        liste.append(produit.capitalize())
        
def supprimer_produit(liste):
    produit = input("Quel produit voulez-vous supprimer (nom ou position dans la liste) ? ")
    if len(liste) == 0 :
        print("Il n'est pas possible de supprimer un produit dans une liste vide !")
    elif produit.isdigit() and int(produit) < (len(liste)+1):
        element = liste.pop(int(produit) - 1)
        print(f"{element.upper()} a été supprimé de la liste")
    elif produit.capitalize() in liste:
        liste.remove(produit.capitalize())
        print(f"{produit.upper()} a été supprimé de la liste")
    else:
        print("Ce produit n'est pas présent dans votre liste de course")

def vider_liste (liste):
    liste.clear()
    print("Suppression de la liste de course")

def choix_compris_dans_menu (menu, choix):
    liste_choix = string.ascii_lowercase[:len(menu)]
    retour = False
    if choix in liste_choix:
        retour = True
    return retour


quitter = False

while quitter == False:
    afficher_menu(menu)
    choix = input("Quelle action souhaitez-vous effectuer (lettre du choix) ?")
    if choix_compris_dans_menu(menu, choix) :
        if choix == 'a':
            afficher_liste_de_course(liste_de_course)
        elif choix == 'b':
            ajouter_produit(liste_de_course)
        elif choix == 'c':
            supprimer_produit(liste_de_course)
        else :
            print("Quitter")
            quitter = True
    else :
        print("Entrez la lettre correspondant à l'action voulue")
        
