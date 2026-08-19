def wecker_decorator(original_funktion):
    def huelle():
        print("⏰ RIIING! Aufwachen!")
        original_funktion()
        print("☀️ Guten Morgen!")
    return huelle

@wecker_decorator
def mache_kaffee():
    print("Kaffee wird gekocht... ☕")

mache_kaffee()