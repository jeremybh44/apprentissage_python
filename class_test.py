class Voiture:
    voitures_crees = 0

    def __init__(self, marque, vitesse, prix):
        Voiture.voitures_crees += 1
        self.marque = marque
        self.vitesse = vitesse
        self.prix = prix

    def __str__(self):  # définir l'affichage de notre objet quand on veut le print ou convertir en str
        return f"Voiture de marque {self.marque} avec vitesse maximale de {self.vitesse}"

    def afficher_marque(self):
        print(f"La voiture est une {self.marque}")

    @classmethod  # méthode associée à la classe
    # Permet de créer un objet avec des éléments définissant les caractéristiques des lamborghini
    def lamborghini(cls):
        return cls(marque="Lamborghini", vitesse=250, prix=200000)

    @classmethod
    def porsche(cls):
        return cls(marque="Porsche", vitesse=200, prix=100000)

    @staticmethod
    def afficher_nombre_voiture():
        print(f"Vous avez {Voiture.voitures_crees} voitures dans votre garage")


if __name__ == "__main__":

    voiture_01 = Voiture.lamborghini()
    voiture_02 = Voiture.porsche()
    print(voiture_01.marque)
    voiture_01.afficher_marque()
    print(voiture_02.marque)
    Voiture.afficher_nombre_voiture()

    affichage = str(voiture_02)
    print(affichage)
