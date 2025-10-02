def diviser(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b


try:
    resultat = diviser(10, 0)
    print(f"Résultat: {resultat}")

except ValueError as e:
    print(f"Erreur: {e}")

try:
    resultat = diviser(10, 2)
    print(f"Résultat: {resultat}")
except ValueError as e:
    print(f"Erreur: {e}")
