from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base 

Base = declarative_base()

class Kunde(Base):
        __tablename__ = "kunde"
        id = Column(Integer, primary_key=True)
        name = Column(String)
        email = Column(String)



class Bestellung(Base): 
        __tablename__ = "bestellung"
        id = Column(Integer, primary_key=True)
        produkt = Column(String)
        preis = Column(Float)
        kunde_id = Column(Integer, ForeignKey("kunde.id"))