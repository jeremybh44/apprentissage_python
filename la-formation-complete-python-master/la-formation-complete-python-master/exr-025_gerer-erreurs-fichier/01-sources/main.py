fichier = input("Entrez le chemin du fichier à lire : ")

try:
    flux = open(fichier, "r")
    print(flux.read())
except FileNotFoundError:
    print("Fichier introuvable")
except UnicodeDecodeError:
    print("Impossible de lire le fichier")
else:
    flux.close()
    
    


