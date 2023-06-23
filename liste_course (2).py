import sys

# Définition de tous les sous-menu
SOUS_MENU_AFFICHER = "afficher la liste de course"
SOUS_MENU_AJOUT    = "ajouter un produit"
SOUS_MENU_RETRAIT  = "supprimer un produit"
SOUS_MENU_VIDER    = "supprimer la liste de course"
SOUS_MENU_QUITTER  = "quitter"

# Définition du menu
MENU = (SOUS_MENU_AJOUT, SOUS_MENU_RETRAIT, SOUS_MENU_AFFICHER, SOUS_MENU_VIDER, SOUS_MENU_QUITTER)

# Définition de la liste de course
liste_course = []

# Fonction pour afficher le menu
def afficher_menu ():
    print("========== MENU ==========")
    for i,sous_menu in enumerate(MENU):
        print(f"{i+1}. \t{sous_menu.capitalize()}")
    print("==========================")

# Fonction pour afficher la liste de course
def afficher_liste():
    print("----- LISTE DE COURSE ----")
    if len(liste_course) == 0:
        print("Vide")
    else:
        for i,produit in enumerate(liste_course):
            print(f"{i+1}. \t{produit}")
    print("--------------------------")

# Fonction pour vider la liste de course
def vider_liste():
    liste_course.clear()
    print("Suppression de la liste de course")

# Fonction pour ajouter un produit dans la liste de course
def ajouter_produit():
    produit = input("Quel produit voulez-vous ajouter ? ")
    
    # Vérification que l'utilisateur a rentré quelque chose
    if len(produit) == 0:
        print("Produit non renseigné")
    # Vérification qu'il n'y a pas de chiffre dans le nom du produit
    elif any(car.isdigit() for car in produit):
        print("Le produit ne doit pas contenir de chiffre")
    # Vérification que le produit ne se trouve pas déjà dans la liste
    elif produit.capitalize() in liste_course:
        print("Ce produit est déjà présent dans la liste de course")
    else:
        liste_course.append(produit.capitalize())
        print(f"Ajout {produit.capitalize()} dans la liste")

# Fonction pour supprimer un produit de la liste de course
def supprimer_produit():
    produit = input("Quel produit voulez-vous retirer de la liste (position ou nom du produit) ? ")
    
    # Vérification que l'utilisateur a rentré quelque chose
    if len(produit) == 0:
        print("Produit non renseigné")
    # Vérification que l'utilisateur a voulu rentré la position du produit
    elif produit.isdigit():
        index = int(produit) - 1
        # Vérification que la position est n'est pas hors borne
        if index in range(len(liste_course)):
            element = liste_course.pop(index)
            print(f"Retrait de '{element}' de la liste de course")
        else:
            print("Ce produit n'est pas présent dans la liste")
    # Vérification que l'utilisateur a rentré un nom de produit valide
    elif any(car.isdigit() for car in produit):
        print("Le produit ne doit pas contenir de chiffre")
    # Vérifiaction que le produit est présent dans la liste de course
    elif produit.capitalize() in liste_course:
        liste_course.remove(produit.capitalize())
        print(f"Retrait de '{produit.capitalize()}' de la liste de course")
    else:
        print("Ce produit n'est pas présent dans la liste")

# Tant que l'utilisateur veut faire une action, le programme ne se termine pas
while True:
    afficher_menu()
    choix = input("Quelle action voulez-vous effectuer ?")
    
    # Vérification que l'utilisateur a rentré quelque chose
    if len(choix) == 0:
        continue
    # Vérification que l'utilisateur a rentré un chiffre
    elif choix.isdigit():
        index = int(choix) - 1
        
        # Vérification que le choix de l'utilisateur est compris dans la liste des sous-menu
        if index in range(len(MENU)):
            selection = MENU[index]
            if selection == SOUS_MENU_AFFICHER:
                afficher_liste()
            elif selection == SOUS_MENU_AJOUT:
                ajouter_produit()
            elif selection == SOUS_MENU_RETRAIT:
                supprimer_produit()
            elif selection == SOUS_MENU_VIDER:
                vider_liste()
            else:
                print(SOUS_MENU_QUITTER.capitalize())
                sys.exit()