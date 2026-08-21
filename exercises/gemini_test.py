import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Sag Hallo in einem kurzen Satz."
)

print(response.text)