from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.db_models import Base, Kunde, Bestellung

print("1: Imports erfolgreich")

engine = create_engine("sqlite:///data/firma.db")
print("2: Engine erstellt")

Base.metadata.create_all(engine)
print("3: Tabellen erstellt")

with Session(engine) as session:
    anna = Kunde(name="Anna", email="anna@x.ch")
    ben = Kunde(name="Ben", email="ben@x.ch")
    session.add_all([anna, ben])
    session.commit()
    print("4: Kunden eingefügt")

    session.add_all([
        Bestellung(produkt="Laptop", preis=899.0, kunde_id=anna.id),
        Bestellung(produkt="Maus", preis=25.0, kunde_id=anna.id),
        Bestellung(produkt="Tastatur", preis=60.0, kunde_id=ben.id),
    ])
    session.commit()
    print("5: Bestellungen eingefügt")