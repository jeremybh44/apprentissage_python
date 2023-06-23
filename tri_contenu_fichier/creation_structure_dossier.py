"""
Dans cet exercice vous devez :
- Ouvrir le fichier prenoms.txt et lire son contenu.
- Récupérer chaque prénom séparément dans une liste.
- Nettoyer les prénoms pour enlever les virgules, points ou espace.
- Écrire la liste ordonnée et nettoyée dans un nouveau fichier texte.
"""

from encodings import utf_8
from pathlib import Path

# path du script python
chemin_py = Path(__file__)

# path du fichier a trier
fichier_a_trier = Path(chemin_py.parent / "prenoms.txt")

# path du fichier qui contiendra les prenoms tries
fichier_trie = Path(chemin_py.parent / "prenoms_tries.txt")

# recuperation du contenu du fichier
contenu = fichier_a_trier.read_text(encoding="utf-8")

# nettoyage du contenu
contenu = contenu.replace(".", ",")
contenu = contenu.replace(" ", ",")
contenu = contenu.replace("\n", ",")

# creation de la lliste des elements
liste_prenoms_brute = contenu.split(",")

liste_prenom_nettoye = []

# filtrer les elements vides
for prenom in liste_prenoms_brute:
    if prenom is not "":
        liste_prenom_nettoye.append(prenom)

# trier les prenoms par ordre alphabetique
liste_prenom_trie = sorted(liste_prenom_nettoye)

# ecriture de la liste des prenoms tries dans le fichier de destination
fichier_trie.write_text("\n".join(liste_prenom_trie))
