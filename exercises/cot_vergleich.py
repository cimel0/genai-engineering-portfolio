import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])


def frage_ohne_cot(aufgabe: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=aufgabe
        )
        return response.text
    except Exception as e:
        return f"Fehler bei der Anfrage: {e}"


def frage_mit_cot(aufgabe: str) -> str:
    try:
        prompt = aufgabe + "\nDenke Schritt für Schritt."
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Fehler bei der Anfrage: {e}"

aufgaben = [
    "Was ist 15% von 240?",
    "Ein Kunde hat Selbstbehalt CHF 200, Rabatt 10% auf den Selbstbehalt, "
    "Schaden CHF 3450. Wie viel zahlt die Versicherung aus?",
    "Ein Kunde hat eine KFZ-Versicherung mit Selbstbehalt CHF 500. Bei einem "
    "Unfall entsteht ein Schaden von CHF 4200. Der Kunde ist zu 30% mitschuldig, "
    "daher wird die Auszahlung um diesen Anteil gekürzt. Zusätzlich gewährt die "
    "Versicherung einen Treuerabatt von 5% auf die finale Auszahlungssumme, da "
    "der Kunde seit über 10 Jahren Kunde ist. Wie viel zahlt die Versicherung aus?"
]

if __name__ == "__main__":
    for aufgabe in aufgaben:
        print(f"=== Aufgabe: {aufgabe} ===")
        print(f"Ohne CoT: {frage_ohne_cot(aufgabe)}")
        print(f"Mit CoT: {frage_mit_cot(aufgabe)}")
        print()