import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
    model="ft:gpt-3.5-turbo-0613:personal::7r5hcQls",
    messages=[
        {"role": "user", "content": "What's the most popular programming language in the world?"}
    ]
)

print(completion.choices[0].message["content"])
