import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=os.environ["GOOGLE_API_KEY"]
)

zusammenfassung_prompt = ChatPromptTemplate.from_template("fasse '{wort}' zusammen. Nur das Wort.")
risiko_prompt = ChatPromptTemplate.from_template("Nenne die Risikoeinschätzung von '{wort}' in einem Satz.")

parallel_chain = RunnableParallel(
    zusammenfassung=zusammenfassung_prompt | model | StrOutputParser(),
    risiko=risiko_prompt | model | StrOutputParser(),
)

ergebnis = parallel_chain.invoke({"wort": "Der Kunde meldet einen Wasserschaden in der Küche nach einem geplatzten Rohr, geschätzter Schaden 8000 CHF."
})
print(ergebnis)