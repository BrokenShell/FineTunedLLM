import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

result = openai.File.create(file=open("marv.jsonl", "rb"), purpose='fine-tune')
print(result)

file = "file-lyUgIB3OVWvMEZbjMK72NCs8"
