import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda 

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=os.environ["GOOGLE_API_KEY"]
)

def markiere_hohes_risiko(text: str) -> str:
    if "mittleres" in text.lower():
        return f"⚠️ {text}"
    return text

risiko_prompt = ChatPromptTemplate.from_template("Nenne die Risikoeinschätzung von '{schadensfall}' in einem Satz.")

risiko_chain = risiko_prompt | model | StrOutputParser() | RunnableLambda(markiere_hohes_risiko)

ergebnis = risiko_chain.invoke({"schadensfall": "Der Kunde meldet einen Wasserschaden in der Küche nach einem geplatzten Rohr, geschätzter Schaden 8000 CHF."})
print(ergebnis)
