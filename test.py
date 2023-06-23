class Livre:

	def __init__(self, nom, nombre_de_pages, prix):
		self.nom = nom
		self.nombre_de_pages = nombre_de_pages
		self.prix = prix


if __name__ == "__main__":
	livre_HP = Livre(nom="Harry Potter", nombre_de_pages=300, prix=10.99)
	livre_LOTR = Livre(nom="Le Seigneur des Anneaux", nombre_de_pages=400, prix=13.99)

	print(livre_HP)
	print(livre_LOTR)


