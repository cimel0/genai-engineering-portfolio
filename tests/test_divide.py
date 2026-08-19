from exercises.divide import safe_divide


def test_division_erfolgreich():
    assert safe_divide(10, 2) == 5.0


def test_division_durch_null():
    ergebnis = safe_divide(10, 0)
    assert ergebnis == "Division durch Null nicht erlaubt"