
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Explain what a syllabus is in one sentence, like I'm 10 years old.",
)

print(response.text)
