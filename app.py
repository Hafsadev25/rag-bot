import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

print("RAG Bot Ready! Ask a question. Type 'exit' to quit.")

while True:
    user_question = input("\nYou: ")
    if user_question.lower() == 'exit':
        break

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_question}
        ],
    )

    answer = completion.choices[0].message.content
    print(f"\nBot: {answer}")