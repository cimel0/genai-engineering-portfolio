import pytest 
from app.models import Person, PersonValidationError

def test_negativer_preis_wirft_exception():
  with pytest.raises(PersonValidationError): 
    Person(name="Test", alter=-5.0, stadt="München")


def test_person_erfolgreich_erstellt(): 
  p = Person(name="Mira", alter=28, stadt="Zürich")
  assert p.name == "Mira"
  assert p.alter == 28
  assert p.stadt == "Zürich"
  