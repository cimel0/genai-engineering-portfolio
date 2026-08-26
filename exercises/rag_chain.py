import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_chroma import Chroma 
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001", 
    google_api_key=os.environ["GOOGLE_API_KEY"]
)

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=os.environ["GOOGLE_API_KEY"]
)

vector_store = Chroma(
    collection_name="schadensfaelle",
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

retriever = vector_store.as_retriever(search_type="mmr", search_kwargs={"k": 2, "filter": {"schadenstyp": "wasserschaden"}})

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

prompt = ChatPromptTemplate.from_template("""Beantworte die Frage NUR anhand des folgenden Kontexts. Wenn die Antwort nicht im Kontext steht, sag das ehrlich.

Kontext: {kontext}
Frage: {frage}""")

rag_chain = (
    RunnableParallel(kontext=retriever | format_docs, frage=RunnablePassthrough())
    | prompt
    | model
    | StrOutputParser()
)

antwort = rag_chain.invoke("Wie hoch ist der geschätzte Schaden?")
print(antwort)