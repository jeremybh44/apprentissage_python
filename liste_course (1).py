menu = ["afficher la liste de course", "ajouter un produit", "supprimer un produit", "supprimer la liste de course", "quitter"]
liste_course = []
def afficher_menu ():
    print("========== MENU ==========")
    for i in range(len(menu)):
        print(f"{i+1}. \t{menu[i].capitalize()}")
    print("==========================")

def afficher_liste():
    print("========== MENU ==========")
    for i in range(len(menu)):
        print(f"{i+1}. \t{menu[i].capitalize()}")
    print("==========================")
    
afficher_menu()
quitter = False

#while quitter == False:
#    afficher_menu()
#    choix = input 