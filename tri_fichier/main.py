from pathlib import Path

ASSOCIATION_EXT_DOSSIER = {
    ".mp3": "Musique",
    ".wav": "Musique",
    ".flac": "Musique",
    ".avi": "Videos",
    ".mp4": "Videos", 
    ".gif": "Videos",
    ".bmp": "Images",
    ".png": "Images",
    ".jpg": "Images",
    ".txt": "Documents",
    ".pptx": "Documents", 
    ".csv": "Documents", 
    ".xls": "Documents",
    ".odp": "Documents",
    ".pages": "Documents",
}

DOSSIER_A_TRIER = r"C:\Users\GG\Documents\apprentissage_python\tri_fichier\data"

path_dossier_a_trier = Path(DOSSIER_A_TRIER)

liste_fichiers = path_dossier_a_trier.iterdir()

for fichier in liste_fichiers:
    if fichier.is_file():
        dossier_destination = path_dossier_a_trier.parent / ASSOCIATION_EXT_DOSSIER.get(fichier.suffix, "Divers")
        dossier_destination.mkdir(exist_ok=True)
        fichier.rename(dossier_destination / fichier.name)
        