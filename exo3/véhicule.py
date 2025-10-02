class Vehicule:
    def __init__(self, marque: str, modele: str):
        self.marque = marque
        self.modele = modele
class Voiture(Vehicule):
    def __init__(self, marque: str, modele: str, nb_porte: int):
        super().__init__(marque, modele)
        self.porte = nb_porte
class Moto(Vehicule):
    def __init__(self, marque: str, modele: str, type_moteur: str):
        super().__init__(marque, modele)
        self.moteur = type_moteur
audi = Voiture(marque="audi", modele="r8", nb_porte=3)
ducati = Moto(marque="ducati", modele="panigale v4", type_moteur="1000")
print(
    f"La meilleur voiture sur le marché actuelle est la {audi.marque} {audi.modele} {audi.porte} porte"
)
print(
    f"La meilleur moto sur le marché actuelle est la {ducati.marque} {ducati.modele} {ducati.moteur} cc3"
)
