class Voiture:
    roues = 4

    def afficher_roues(self):
        print(f"La voiture a {Voiture.roues} roues.")


voiture_01 = Voiture()
voiture_01.afficher_roues()