import time

import typer

app = typer.Typer()
def main(delete: bool = typer.Option(..., help="Supprime les fichiers trouvées"), extension: str = typer.Argument(..., help="Extension à chercher")):
    """
    Affiche les fichiers trouvés avec l'extension donnée.
    :return:
    """
    prenom_ = "Patrick"
    prenom = typer.style(prenom_, fg=typer.colors.RED, bold=True)
    print(prenom)
    print(delete)
    typer.secho(prenom, fg=typer.colors.BLUE)
    typer.secho(f"Recherche des fichiers avec l'extension {extension}.", fg=typer.colors.BLUE)
    if delete:
        typer.confirm("Souhaitez vous vraiment supprimer les fichiers ?", abort=True)

    print("Suppression des fichiers.")

    liste = range(1000)
    with typer.progressbar(liste) as progress:
        for _ in progress:
            time.sleep(0.001)


@app.command("search")
def search_py():
    main(delete=False, extension="py")


@app.command("delete")
def delete_py():
    main(delete=True, extension="py")


if __name__ == "__main__":
    app()
