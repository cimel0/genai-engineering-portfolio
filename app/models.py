class PersonValidationError(Exception):
    pass


class Person:
    def __init__(self, name: str, alter: int, stadt: str):
        if alter < 0:
            raise PersonValidationError(f"Ungültiges Alter: {alter}")
        self.name = name
        self.alter = alter
        self.stadt = stadt





class ProduktValidationError(Exception):
    pass


class Produkt:
    def __init__(self, name: str, preis: float, kategorie: str):
        if preis < 0:
            raise ProduktValidationError(f"Preis unter 0 ungültig: {preis}")
        self.name = name
        self.preis = preis
        self.kategorie = kategorie