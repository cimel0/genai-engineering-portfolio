fruechte = ["Apfel", "Trauben", "Bananen"]
fruechte.append("Brinen")
print(fruechte)

heute = (2026, 8, 12)
try:
    heute[0] = 2027
except TypeError as e:
    print(f"Erwarteter Fehler: {e}")