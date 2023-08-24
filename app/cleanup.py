import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

print(openai.Model.list(limit=10))
# openai.Model.delete("ft:gpt-3.5-turbo-0613:personal::7qkCBhCH")
# openai.Model.delete("ft:gpt-3.5-turbo-0613:personal::7qlTeHtR")
