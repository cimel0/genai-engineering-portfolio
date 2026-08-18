from app.models import Person, PersonValidationError, Produkt, ProduktValidationError

def lade_produkte_aus_csv(pfad: str) -> list[Produkt]:
    produkte = []
    with open(pfad, "r") as datei:
        for zeile in datei:
            teile = zeile.strip().split(",")
            name = teile[0].strip()
            preis = float(teile[1].strip())
            kategorie = teile[2].strip()
            try:
                produkt = Produkt(name, preis, kategorie)
                produkte.append(produkt)
            except ProduktValidationError as e:
                print(f"Übersprungen: {e}")
    return produkte


def filtere_guenstige_produkte(produkte: list[Produkt], max_preis: float) -> list[Produkt]:
    return [p for p in produkte if p.preis <= max_preis]




def lade_personen_aus_csv(pfad: str) -> list[Person]:
    personen = []
    with open(pfad, "r") as datei:
        for zeile in datei:
            teile = zeile.strip().split(",")
            name = teile[0].strip()
            alter = int(teile[1].strip())
            stadt = teile[2].strip()
            try:
                person = Person(name, alter, stadt)                    
                personen.append(person)
            except PersonValidationError as e:
                print(f"Übersprungen: {e}")
    return personen


def filtere_nach_alter(personen: list[Person], min_alter: int) -> list[Person]:
    return [p for p in personen if p.alter >= min_alter]                                       