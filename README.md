
# GenAI Engineering Portfolio

Ein wachsendes Projekt zur Verbindung von Python, SQL und (bald) GenAI/RAG-Systemen, von Datenverarbeitung über relationale Datenbanken bis hin zu LLM-gestützten Anwendungen.


## Author
- [@cimel0](https://www.github.com/cimel0)

## Tech Stack
Python, SQL, SQLAlchemy

## Projektstruktur
- `app/` — Datenmodelle (Person, Produkt, Kunde, Bestellung) und SQLAlchemy-Anbindung an eine lokale SQLite-Datenbank
- `exercises/` — Einzelne Konzept-Übungen (Decorators, Generators, Context Manager) aus der Lernphase
- `data/` — CSV-Testdaten und lokale SQLite-Datenbank
- `sql/` — SQL-Übungen (Joins, CTEs, Window Functions, Aggregation)
## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Usage

Datenbank initialisieren (einmalig, erstellt Tabellen und Testdaten):
```bash
python3 -m app.db_setup
```

Beispielabfragen ausführen (zeigt Bestellungen mit Kundennamen sowie Gesamtausgaben pro Kunde):
```bash
python3 db_main.py
```
## Status / Roadmap
- ✅ Python-Fundamentals
- ✅ SQL & SQLAlchemy
- 🔄 GenAI/RAG (in Arbeit)
- ⬜ Cloud-Deployment (GCP)