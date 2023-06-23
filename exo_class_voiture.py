LIMITE_FAIRE_PLEIN = 10
CAPACITE_RESERVOIR = 100

class Voiture:

    def __init__(self):
        """Initialisation de chaque instance de voiture avec la capacité maximale du réservoir d'essence"""
        self.essence = CAPACITE_RESERVOIR

    def afficher_reservoir(self):
        """Afficher la quantité d'essence restante dans la voiture

        Returns :
            Rien
        """
        print(f"La voiture contient {self.essence} litres d'essence")

    def roule(self, km):
        """Mise à jour du niveau d'essence dans le cas où il en reste assez pour rouler le nombre de kilomètres souhaité

        Args :
            km : nombre de kilomètres à parcourir

        Returns :
            Rien
        """
        # Calcul de la consommation d'essence selon le nombre de kilomètres à parcourir
        consommation = (km * 5) / 100
        print(consommation)
        # Vérification qu'il y a assez d'essence dans la voiture
        if consommation < self.essence:
            # Soustraction de la consommation à l'essence restant dans la voiture
            self.essence -= consommation
        else:
            print("Vous n'avez plus d'essence, faites le plein !")

        # Prévenir s'il faut faire le plein
        if self.essence < LIMITE_FAIRE_PLEIN:
            print("Vous n'avez bientôt plus d'essence !")

    def faire_le_plein(self):
        """Remplis le réservoir d'essence au maximum de sa capacité

        Returns :
            Rien
        """
        self.essence = CAPACITE_RESERVOIR
        print("Vous pouvez repartir !")


if __name__ == "__main__":
    voiture = Voiture()

    voiture.afficher_reservoir()

    voiture.roule(km=10)

    voiture.afficher_reservoir()

    voiture.faire_le_plein()

    voiture.afficher_reservoir()

    voiture.roule(km=1900)

    voiture.afficher_reservoir()
