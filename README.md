# GenAI Engineering Portfolio

Ein strukturiert aufgebautes Projekt zur Vertiefung von Software Engineering, Datenbanken und Generative-AI-Engineering — von Python-Grundlagen über relationale Datenmodellierung bis zu einem selbst entwickelten RAG-System (Retrieval-Augmented Generation).

## Author
- [@cimel0](https://www.github.com/cimel0)

## Tech Stack
Python, SQL (PostgreSQL, SQLite), LangChain (LCEL), Google Gemini API, Chroma (Vector Database), Git-Flow, GitHub Actions (CI/CD), Docker

## Highlights

**RAG-System von Grund auf entwickelt:** Dokumente werden geladen und in überlappende Chunks zerlegt, per Google-Gemini-Embeddings in Vektoren umgewandelt und in einer Chroma-Vektordatenbank gespeichert (inkl. Metadata-Filtering, z. B. nach Schadenstyp). Eine LCEL-Chain verbindet Retriever, Prompt und LLM zu einem vollständigen Frage-Antwort-System, das ausschliesslich auf Basis der gefundenen Dokumente antwortet.

**Sauberes Software Engineering statt reinem Prompting:** Jede Änderung läuft über Git-Flow (Feature-Branches, Pull Requests, CI-Pipeline via GitHub Actions), die vor jedem Merge grün sein muss.

**Systematisches Debugging & Evaluation:** Unter anderem ein dokumentierter Fall, in dem ein LLM bei einer komplexen Chain-of-Thought-Aufgabe eine falsche Rechenreihenfolge selbstständig als "Standard-Praxis" deklarierte — ein reales, selbst gefundenes Halluzinations-Beispiel, das die Bedeutung von Evaluation zusätzlich zu reinem Bauen zeigt.

## Projektstruktur
- `app/` — Datenmodelle (Person, Produkt, Kunde, Bestellung) und SQLAlchemy-Anbindung an eine lokale SQLite-Datenbank
- `exercises/` — Einzelübungen entlang des Lernpfads: Python-Grundlagen (Decorators, Generators, Context Manager), GenAI-Konzepte (Temperature/Softmax, Cosine Similarity, Chain-of-Thought), LCEL-Bausteine (erste Chain, RunnableParallel, RunnableLambda), RAG-Pipeline (Chunking, Embeddings, Metadata-Filtering, komplette RAG-Chain)
- `data/` — CSV-Testdaten, Beispieltexte für RAG (Schadensfall-Szenarien) und lokale SQLite-Datenbank
- `sql/` — SQL-Übungen (Joins, CTEs, Window Functions, Aggregation) sowie rohes DDL mit Entity-/Referential-Integrity-Constraints (ER-Modellierung, Foreign Keys, CHECK-Constraints)

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Für die GenAI-Übungen wird ein Google-Gemini-API-Key benötigt (kostenloses Kontingent). In einer lokalen `.env`-Datei (gitignored) hinterlegen:
```
GOOGLE_API_KEY=dein-api-key
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

RAG-System ausführen (lädt Beispieldokumente, baut den Vector Store auf, beantwortet eine Beispielfrage ausschliesslich basierend auf dem gefundenen Kontext):
```bash
python3 exercises/rag_chain.py
```

## Architektur: RAG-Pipeline im Überblick

1. **Ingestion:** Dokumente laden (`TextLoader`) → in überlappende Chunks zerlegen (`RecursiveCharacterTextSplitter`)
2. **Indexierung:** Jeder Chunk wird per Gemini-Embeddings vektorisiert und in Chroma gespeichert, inkl. Metadata (z. B. `schadenstyp`) für spätere Filterung
3. **Retrieval:** Eine Nutzerfrage wird ebenfalls vektorisiert; Chroma liefert die semantisch ähnlichsten Chunks zurück, optional eingeschränkt per Metadata-Filter
4. **Generation:** Gefundene Chunks + Originalfrage werden in einen Prompt eingebettet; das LLM generiert eine Antwort ausschliesslich basierend auf diesem Kontext, nicht aus eigenem Vorwissen

## Limitierungen & mögliche Verbesserungen

- Aktuell nur ein kleines, manuell erstelltes Test-Textkorpus (Schadensfall-Beispiele) — noch keine Evaluation auf einem grösseren, realistischen Datensatz
- Kein Reranking-Schritt nach dem initialen Retrieval; bei grösseren Dokumentenmengen würde das die Präzision weiter verbessern
- Keine automatisierten RAGAS-Metriken (Context Precision/Recall, Faithfulness, Answer Relevancy) integriert — aktuell nur manuelle, stichprobenartige Prüfung
- Chunking-Parameter (`chunk_size`, `chunk_overlap`) sind statisch gewählt, nicht empirisch auf Retrieval-Qualität optimiert
- Noch kein Cloud-Deployment (geplant: GCP, passend zum genutzten Gemini-Ökosystem)

## Status / Roadmap
- ✅ Python-Fundamentals (OOP, Decorators, Generators, Context Manager, Type Hints)
- ✅ SQL & SQLAlchemy (Joins, CTEs, Window Functions, Normalisierung, ER-Modellierung, rohes DDL)
- ✅ Git-Flow, CI/CD (GitHub Actions), Docker
- ✅ GenAI-Fundamentals (Tokens, Attention, Prompting, CoT, ReAct, RAG-Architektur, Embeddings, RAGAS-Konzepte)
- ✅ LangChain/LCEL & RAG-System (Chunking, Embeddings, Chroma Vector Store, Metadata-Filtering, vollständige RAG-Chain)
- 🔄 Agents & Tool Calling (LangGraph) — in Arbeit
- ⬜ Tiny-Transformer-Sprachmodell from Scratch (PyTorch)
- ⬜ Cloud-Deployment (GCP)

## Kontakt
Fragen? Gerne über GitHub.

Letzte Aktualisierung: August 2026