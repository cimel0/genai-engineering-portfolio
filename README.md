# GenAI Engineering Portfolio

A structured project built to develop depth in software engineering, databases, and generative AI engineering, from Python fundamentals through relational data modeling to a self-built RAG system (Retrieval-Augmented Generation).

## Author
- [@cimel0](https://www.github.com/cimel0)

## Tech Stack
Python, SQL (PostgreSQL, SQLite), LangChain (LCEL), Google Gemini API, Chroma (Vector Database), Git-Flow, GitHub Actions (CI/CD), Docker

## Highlights

**RAG system built from the ground up:** Documents are loaded and split into overlapping chunks, embedded into vectors via Google Gemini embeddings, and stored in a Chroma vector database with metadata filtering (e.g. by claim type). An LCEL chain connects retriever, prompt, and LLM into a complete question-answering system that only answers based on retrieved documents.

**Real software engineering, not just prompting:** Every change goes through a Git-Flow workflow (feature branches, pull requests, a CI pipeline via GitHub Actions) that has to pass before anything gets merged.

**Systematic debugging and evaluation:** Including a documented case where an LLM, given a complex Chain-of-Thought task, picked a calculation order on its own and labeled it "standard practice" in insurance, a real, self-discovered hallucination example that shows why evaluation matters as much as building.

## Project Structure
- `app/` — data models (Person, Product, Customer, Order) and SQLAlchemy connection to a local SQLite database
- `exercises/` — individual exercises along the learning path: Python fundamentals (decorators, generators, context managers), GenAI concepts (temperature/softmax, cosine similarity, Chain-of-Thought), LCEL building blocks (first chain, RunnableParallel, RunnableLambda), RAG pipeline (chunking, embeddings, metadata filtering, full RAG chain)
- `data/` — CSV test data, sample texts for RAG (insurance claim scenarios), and local SQLite database
- `sql/` — SQL exercises (joins, CTEs, window functions, aggregation) plus raw DDL with entity and referential integrity constraints (ER modeling, foreign keys, CHECK constraints)

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

The GenAI exercises need a Google Gemini API key (free tier). Add it to a local `.env` file (gitignored):
```
GOOGLE_API_KEY=your-api-key
```

## Usage

Initialize the database (one-time, creates tables and test data):
```bash
python3 -m app.db_setup
```

Run sample queries (shows orders with customer names and total spending per customer):
```bash
python3 db_main.py
```

Run the RAG system (loads sample documents, builds the vector store, answers a sample question based only on the retrieved context):
```bash
python3 exercises/rag_chain.py
```

## Architecture: RAG Pipeline Overview

1. **Ingestion:** Load documents (`TextLoader`) and split them into overlapping chunks (`RecursiveCharacterTextSplitter`)
2. **Indexing:** Each chunk is embedded via Gemini embeddings and stored in Chroma, along with metadata (e.g. `claim_type`) for later filtering
3. **Retrieval:** A user question is embedded the same way; Chroma returns the most semantically similar chunks, optionally restricted by a metadata filter
4. **Generation:** Retrieved chunks and the original question are inserted into a prompt; the LLM generates an answer based only on this context, not on its own prior knowledge

## Limitations & Possible Improvements

- Currently only a small, manually created test corpus (insurance claim examples); no evaluation yet on a larger, realistic dataset
- No reranking step after initial retrieval; this would improve precision further on larger document sets
- No automated RAGAS metrics (Context Precision/Recall, Faithfulness, Answer Relevancy) integrated yet, only manual spot-checking so far
- Chunking parameters (`chunk_size`, `chunk_overlap`) are set statically rather than tuned empirically against retrieval quality
- No cloud deployment yet (planned: GCP, matching the Gemini ecosystem already in use)

## Status / Roadmap
- ✅ Python fundamentals (OOP, decorators, generators, context managers, type hints)
- ✅ SQL & SQLAlchemy (joins, CTEs, window functions, normalization, ER modeling, raw DDL)
- ✅ Git-Flow, CI/CD (GitHub Actions), Docker
- ✅ GenAI fundamentals (tokens, attention, prompting, CoT, ReAct, RAG architecture, embeddings, RAGAS concepts)
- ✅ LangChain/LCEL & RAG system (chunking, embeddings, Chroma vector store, metadata filtering, full RAG chain)
- 🔄 Agents & tool calling (LangGraph), in progress
- ⬜ Tiny transformer language model from scratch (PyTorch)
- ⬜ Cloud deployment (GCP)

## Contact
Questions? Feel free to reach out via GitHub.

Last updated: August 2026
