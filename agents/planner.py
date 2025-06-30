import os
from dotenv import load_dotenv
from openai import OpenAI

# Force load the .env file
load_dotenv()

# Check if the variable is actually loaded
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise Exception("⚠️ OPENAI_API_KEY not loaded. Please check your .env file.")

client = OpenAI(api_key=api_key)

def plan_task(user_input):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a planning assistant that breaks real-world tasks into simple, sequential subtasks."},
            {"role": "user", "content": f"Break this down into subtasks: {user_input}"}
        ]
    )

    output = response.choices[0].message.content.strip()
    return output.split("\n")


