etudiants = [
    {"nom": "Alice", "note": 15, "annee": 2},
    {"nom": "Peter", "note": 12, "annee": 1},
    {"nom": "Ange", "note": 5, "annee": 2},
    {"nom": "Angie", "note": 20, "annee": 3},
    {"nom": "Pa", "note": 3, "annee": 2},
    {"nom": "Florian", "note": 20, "annee": 3},
    {"nom": "Evan", "note": 18, "annee": 1},
]
admis = [e["nom"] for e in etudiants if e["note"] >= 12]
admis2 = list(filter(lambda x: x["note"] >= 12, etudiants))
print(admis)
array = set([element["annee"] for element in etudiants])
moyenne_anne = {
    element: sum([annee["note"] for annee in etudiants if annee["annee"] == element])
    / len([annee["note"] for annee in etudiants if annee["annee"] == element])
    for element in array
}
print(moyenne_anne)
def mention(note: int):
    if note > 16:
        return "Très bien"
    elif 16 > note >= 14:
        return "bien"
    elif 14 > note >= 12:
        return "Assez bien"
    elif 12 > note >= 10:
        return "Admis"
    elif 10 > note:
        return "Recale"
mentionne = {element["nom"]: mention(element["note"]) for element in etudiants}
print(mentionne)
