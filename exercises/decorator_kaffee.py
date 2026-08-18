def wecker_decorator(original_funktion):
    # Das ist die Hülle (Verpackung)
    def huelle():
        print("⏰ RIIING! Aufwachen!") # Vorher
        original_funktion()            # Die eigentliche Arbeit
        print("☀️ Guten Morgen!")       # Nachher
    
    return huelle # Wir geben die fertig verpackte Funktion zurück

@wecker_decorator
def mache_kaffee():
    print("Kaffee wird gekocht... ☕")
