def gerade_zahlen(max_wert):
    for i in range(max_wert):
        if i % 2 == 0:              # Lücke 1: Bedingung "i ist gerade"
            yield i         # Lücke 2: welcher Wert wird geliefert?

for zahl in gerade_zahlen(10):
    print(zahl)