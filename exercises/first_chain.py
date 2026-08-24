import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=os.environ["GOOGLE_API_KEY"]
)

prompt = ChatPromptTemplate.from_template("Erkläre {thema} in einem Satz.")
chain = prompt | model | StrOutputParser()

ergebnis = chain.invoke({"thema": "Photosynthese"})
print(ergebnis)
