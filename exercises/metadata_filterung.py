import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001", 
    google_api_key=os.environ["GOOGLE_API_KEY"]
    )

# Wasserschaden laden, splitten, taggen
loader_wasser = TextLoader("data/schadensfall_beispiel.txt")
chunks_wasser = RecursiveCharacterTextSplitter(chunk_size=60, chunk_overlap=20).split_documents(loader_wasser.load())
for chunk in chunks_wasser:
    chunk.metadata["schadenstyp"] = "wasserschaden"

# Brandschaden laden, splitten, taggen (gleiches Muster, andere Datei/Typ)
loader_brand = TextLoader("data/schadensfall_brand.txt")
chunks_brand = RecursiveCharacterTextSplitter(chunk_size=60, chunk_overlap=20).split_documents(loader_brand.load())
for chunk in chunks_brand:
    chunk.metadata["schadenstyp"] = "brandschaden"

alle_chunks = chunks_wasser + chunks_brand

vector_store = Chroma.from_documents(
    documents=alle_chunks,
    embedding=embeddings,
    collection_name="schadensfaelle",
    persist_directory="./chroma_db",
    collection_metadata={"hnsw:space": "cosine"}
)

frage = "Wie hoch ist der geschätzte Schaden?"
ergebnisse = vector_store.similarity_search_with_score(frage, k=3, filter={"schadenstyp": "brandschaden"})

for doc, distanz in ergebnisse:
    similarity = 1 - distanz
    print(f"Similarity: {similarity:.3f} — {doc.page_content}")