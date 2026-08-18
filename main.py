from app.loader import lade_personen_aus_csv, filtere_nach_alter, lade_produkte_aus_csv, filtere_guenstige_produkte

if __name__ == "__main__":
    personen = lade_personen_aus_csv("data/personen.csv")
    gefiltert_p = filtere_nach_alter(personen, min_alter=18)
    for p in gefiltert_p:
        print(p.name, p.alter, p.stadt)

    produkte = lade_produkte_aus_csv("data/produkt.csv")
    gefiltert_pr = filtere_guenstige_produkte(produkte, max_preis=500.0)
    for pr in gefiltert_pr:
        print(pr.name, pr.preis, pr.kategorie)