from random import choice


class Livre:
    def __init__(self, titre: str, auteur: str, isbn: str):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn

    def __str__(self):
        return self.titre


class LivreNumérique(Livre):
    def __init__(self, titre: str, auteur: str, isbn: str, taille_fichier: int):
        super().__init__(titre, auteur, isbn)
        self.taille = taille_fichier


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


livre1 = Livre("bla", "bli", "987")
livre2 = Livre("lol0", "lille", "654")
livre3 = LivreNumérique("la mort", "voltaire", "6584", 5)
livre4 = Livre("la vie", "voltaire", "65874")
biblio1 = Bibliothèque("pop")
for i in range(55):
    livre = Livre(
        choice(
            [
                "le hobbi",
                "karaté kid",
                "les 2 tour",
                "blanche fesses et les 7 mains",
                "cars",
                "cars 2",
                "cars 3",
                "Alad'1",
            ]
        ),
        choice(
            [
                "stendhale",
                "adolf",
                "zemmour",
                "melanchon",
                "macron",
                "lasalle",
                "staline",
                "huile moteur",
            ]
        ),
        i,
    )
    biblio1.ajouter(livre)
# biblio1.ajouter(livre1)
# biblio1.ajouter(livre2)
# biblio1.ajouter(livre3)
# biblio1.ajouter(livre4)
# biblio1.supprimer_isbn("987")
# biblio1.ajouter(livre1)
# biblio1.rechercher_auteur("voltaire")
biblio1.rechercher_auteur("lasalle")
biblio1.rechercher_titre("cars 2")
# biblio1.rechercher_isbn("654")
# biblio1.rechercher_titre("bla")
