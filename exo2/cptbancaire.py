class CompteBancaire:
    def __init__(self, titulaire: str, solde_initial: float = 0):
        self.titulaire = titulaire
        self.solde = solde_initial

    def deposer(self, montant: float):
        self.solde += montant
        print(f"Vous venez de déposer {montant}€")
        print(f"Votre nouveau solde est{self.solde}€")

    def retirer(self, montant: float):
        if self.solde >= montant:
            self.solde -= montant
            print(f"Vous venez de retirer {montant}€")
            print(f"Votre nouveau solde est {self.solde}€")
        else:
            print(
                f"Vous n'avez pas faire se retrait vous n'avez que {self.solde}€ sur votre compte"
            )

    def afficher(self):
        print(f"Vous avez {self.solde}€ sur votre compte ")


mon_compte = CompteBancaire("Florian", 500)
mon_compte.afficher()
mon_compte.deposer(500)
mon_compte.retirer(10000)
mon_compte.retirer(1)
mon_compte.retirer(999)
