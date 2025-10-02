import csv
import json


class Livre:
    def __init__(self, titre: str, auteur: str, isbn: str):
        self.type = "papier"
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn

    # def __str__(self):
    #     return self.titre


class Livrenumerique(Livre):
    def __init__(self, titre: str, auteur: str, isbn: str, taille_fichier: int):
        super().__init__(titre, auteur, isbn)
        self.taille = taille_fichier
        self.type = "numerique"


class Bibliothèque:
    def __init__(self, nom: str):
        self.livres = []
        self.nom = nom

    def ajouter(self, livre):
        self.livres.append(livre)

    def supprimer_isbn(self, code: str):
        for i in self.livres:
            if i.isbn == code:
                self.livres.remove(i)
                break

    def rechercher_isbn(self, code: str):
        liste_resultat = []
        for i in self.livres:
            if i.isbn == code:
                print(f"{i.titre} {i.auteur} {i.isbn}")
                liste_resultat.append(i)
        return liste_resultat

    def rechercher_auteur(self, auteur: str):
        liste_resultat = []
        for i in self.livres:
            if i.auteur == auteur:
                print(f"{i.titre} {i.auteur} {i.isbn}")
                liste_resultat.append(i)
        return liste_resultat

    def rechercher_titre(self, titre: str):
        liste_resultat = []
        for i in self.livres:
            if i.titre == titre:
                print(f"{i.titre} {i.auteur} {i.isbn}")
                liste_resultat.append(i)
        return liste_resultat

    def afficher(self):
        print(str(self.livres))

    def exporter_csv(self):
        with open(
            "exo6_j2/data/export.csv", "w", newline="", encoding="utf-8"
        ) as fichier:
            writer = csv.DictWriter(
                fichier, fieldnames=["type", "titre", "auteur", "isbn", "taille"]
            )
            writer.writeheader()
            for i in self.livres:
                if i.type == "papier":
                    liste = {
                        "type": "papier",
                        "titre": i.titre,
                        "auteur": i.auteur,
                        "isbn": i.isbn,
                        "taille": "N/A",
                    }
                else:
                    liste = {
                        "type": "numerique",
                        "titre": i.titre,
                        "auteur": i.auteur,
                        "isbn": i.isbn,
                        "taille": i.taille,
                    }

                writer.writerow(liste)

    def exporter_json(self):
        liste = []
        with open("exo6_j2/data/data.json", "w") as f:
            for i in self.livres:
                if i.type == "papier":
                    liste.append(
                        {
                            "type": "papier",
                            "titre": i.titre,
                            "auteur": i.auteur,
                            "isbn": i.isbn,
                        }
                    )
                else:
                    liste.append(
                        {
                            "type": "numerique",
                            "titre": i.titre,
                            "auteur": i.auteur,
                            "isbn": i.isbn,
                            "taille": i.taille,
                        }
                    )
            json.dump(liste, f, indent=2)

    def charger_json(self):
        with open("exo6_j2/data/data.json", "r") as f:
            data = json.load(f)
        for i in range(len(data)):
            if data[i]["type"] == "papier":
                livre = Livre(data[i]["titre"], data[i]["auteur"], data[i]["isbn"])
                self.ajouter(livre)
            else:
                livre = Livrenumerique(
                    data[i]["titre"],
                    data[i]["auteur"],
                    data[i]["isbn"],
                    data[i]["taille"],
                )
                self.ajouter(livre)


livre1 = Livre("bla", "bli", "987")
livre2 = Livre("lol0", "lille", "654")
livre3 = Livrenumerique("la mort", "voltaire", "6584", 5)
livre4 = Livre("la vie", "voltaire", "65874")
biblio1 = Bibliothèque("pop")
biblio2 = Bibliothèque("poper")
# biblio1.ajouter(livre1)
# biblio1.ajouter(livre2)
# biblio1.ajouter(livre3)
# biblio1.ajouter(livre4)
# biblio1.supprimer_isbn("987")
# biblio1.ajouter(livre1)
# biblio1.rechercher_auteur("voltaire")
# biblio1.exporter_csv()
# biblio1.exporter_json()
biblio2.charger_json()
biblio2.afficher()
biblio2.rechercher_auteur("voltaire")
