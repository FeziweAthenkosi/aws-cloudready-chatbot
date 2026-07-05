# importing necessary packages/modelues 
import os
from dotenv import load_dotenv
from groq import Groq
from prompts import create_prompt

#loading the environment variables
load_dotenv()

# Retrieving Groq API Key

groq_api_key = os.getenv("GROQ_API_KEY")
model_name = os.getenv("MODEL_NAME")

# Checking if the Groq API key exists
if groq_api_key:
    print("✅ Groq API Key loaded successfully!")
    print(f"API Key starts with: {groq_api_key[:10]}...")
else:
    print("❌ API Key not found.")

# Retrieving Model Name 
if model_name:
    print("✅ Groq Model Name loaded successfully!")
else:
    print("❌ Model name not found.")

#Creating the Groq client: This authenticates your application using your API key.

client = Groq(api_key=groq_api_key)

print("➡️ Sending request to Groq...")


#Sending the prompt
def ask_groq(prompt):
    #Sends a prompt to Groq and returns the response.
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content

prompt = """
You are an AWS Certified Cloud Practitioner instructor.

Generate ONE high-quality AWS Cloud Practitioner multiple-choice question.

Requirements:

Service:
Amazon EC2

Difficulty:
Easy

Provide:

1. One question.

2. Four options labelled A, B, C and D.

3. Exactly one correct answer.

4. Explain why the correct answer is correct.

5. Explain why every incorrect option is incorrect.

6. Provide one AWS Cloud Practitioner exam tip.

The explanations should be educational because the learner is studying for the exam.

Format the response using headings.

Do not generate JSON.
"""

answer = ask_groq(prompt)

#print the response of the prompt
print(answer)

from config import *

print(DEFAULT_SERVICE)