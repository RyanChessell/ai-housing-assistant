import os
from dotenv import load_dotenv
from openai import OpenAI
from user_profile import user_profile

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def fill_form(resources):
    prompt = f"""
You are an assistant helping fill out a public housing application based on the following user data and application requirements.

User Profile:
{user_profile}

Application Requirements and Info:
{resources}

Please generate a dictionary of completed form fields. Be specific and realistic.
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You complete government forms using structured JSON outputs."},
            {"role": "user", "content": prompt}
        ]
    )

    output = response.choices[0].message.content.strip()

    return {
        "form_status": "filled",
        "fields": output,
        "note": "Form auto-filled by GPT using user profile + housing info"
    }

