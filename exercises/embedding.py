import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from cosine_similarity import cosine_similarity

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    google_api_key=os.environ["GOOGLE_API_KEY"]
)

loader = TextLoader("data/schadensfall_beispiel.txt")
dokumente = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=60, chunk_overlap=20)
chunks = splitter.split_documents(dokumente)

frage = "Wie hoch ist der geschätzte Schaden?"
frage_vektor = embeddings.embed_query(frage)

for chunk in chunks:
    chunk_vektor = embeddings.embed_query(chunk.page_content)
    ähnlichkeit = cosine_similarity(frage_vektor, chunk_vektor)
    print(f"{ähnlichkeit:.3f} — {chunk.page_content}")