import math

def softmax_mit_temperature(logits: dict[str, float], temperature: float) -> dict[str, float]:
    skaliert = {wort: logit / temperature for wort, logit in logits.items()}
    exp_werte = {wort: math.exp(wert) for wort, wert in skaliert.items()}
    summe = sum(exp_werte.values())
    return {wort: wert / summe for wort, wert in exp_werte.items()}

if __name__ == "__main__":
    logits = {"blau": 5.0, "grau": 3.0, "Bananenkuchen": 0.1}
    print(softmax_mit_temperature(logits, 1.0))
    print(softmax_mit_temperature(logits, 0.5))
    print(softmax_mit_temperature(logits, 2.0))