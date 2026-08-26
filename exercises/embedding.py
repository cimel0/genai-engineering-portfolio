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

loader = TextLoader("data/schadensfall_beispiel.txt")
dokumente = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=20)
chunks = splitter.split_documents(dokumente)

vector_store = Chroma.from_documents(documents=chunks, embedding=embeddings)

frage = "Wie hoch ist der geschätzte Schaden?"
ergebnisse = vector_store.similarity_search(frage, k=2)

for doc in ergebnisse:
    print(doc.page_content)