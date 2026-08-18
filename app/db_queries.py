from sqlalchemy import func
from sqlalchemy.orm import Session
from app.db_models import Kunde, Bestellung


def hole_bestellungen_mit_kunde(session: Session) -> list[tuple[str, str, float]]:
    return (
        session.query(Kunde.name, Bestellung.produkt, Bestellung.preis)
        .join(Bestellung, Kunde.id == Bestellung.kunde_id)
        .all()
    )


def hole_gesamtausgaben_pro_kunde(session: Session) -> list[tuple[str, float]]:
    return (
        session.query(Kunde.name, func.sum(Bestellung.preis))
        .join(Bestellung, Kunde.id == Bestellung.kunde_id)
        .group_by(Kunde.name)
        .all()
    )