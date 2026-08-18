from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()

class Mitarbeiter(Base):
    __tablename__ = "mitarbeiter"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    gehalt = Column(Float)
    abteilung = Column(Integer)

engine = create_engine("sqlite:///firma.db")

with Session(engine) as session:
    mitarbeiter_liste = (
        session.query(Mitarbeiter)
        .filter(Mitarbeiter.gehalt > 5000)
        .filter(Mitarbeiter.abteilung == 5)
        .all()
    )
    for m in mitarbeiter_liste:
        print(m.name, m.gehalt, m.abteilung)

