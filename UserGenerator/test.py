class Voiture:
    prix = 30000

    def __init__(self, prix):
        self.prix = prix


Peugeot = Voiture(prix=20000)

print(Peugeot.prix)