"""
=========================================================
Groq Client

Handles communication with the Groq API.
=========================================================
"""

import os

from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found.")

if not MODEL_NAME:
    raise ValueError("MODEL_NAME not found.")

client = Groq(
    api_key=GROQ_API_KEY
)


def generate_response(prompt):
    """
    Sends a prompt to Groq and returns the response.
    """

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content