from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.db_queries import hole_bestellungen_mit_kunde, hole_gesamtausgaben_pro_kunde

engine = create_engine("sqlite:///data/firma.db")

if __name__ == "__main__":
    with Session(engine) as session:
        print("--- Bestellungen mit Kunde ---")
        for name, produkt, preis in hole_bestellungen_mit_kunde(session):
            print(name, produkt, preis)

        print("--- Gesamtausgaben pro Kunde ---")
        for name, summe in hole_gesamtausgaben_pro_kunde(session):
            print(name, summe)