from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()


class Mitarbeiter(Base):
    __tablename__ = "mitarbeiter"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    gehalt = Column(Float)
    abteilung = Column(Integer)


engine = create_engine("sqlite:///data/demo_firma.db")
Base.metadata.create_all(engine)

with Session(engine) as session:
    if not session.query(Mitarbeiter).first():
        session.add_all([
            Mitarbeiter(name="Anna", gehalt=5500.0, abteilung=5),
            Mitarbeiter(name="Ben", gehalt=4500.0, abteilung=5),
            Mitarbeiter(name="Clara", gehalt=6000.0, abteilung=3),
        ])
        session.commit()

    mitarbeiter_liste = (
        session.query(Mitarbeiter)
        .filter(Mitarbeiter.gehalt > 5000)
        .filter(Mitarbeiter.abteilung == 5)
        .all()
    )
    for m in mitarbeiter_liste:
        print(m.name, m.gehalt, m.abteilung)