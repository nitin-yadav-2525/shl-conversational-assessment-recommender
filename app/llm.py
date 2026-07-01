import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Gemini API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Model
model = genai.GenerativeModel("gemini-2.0-flash")


def ask_llm(prompt: str) -> str:
    """
    Send prompt to Gemini and return response text.
    """

    try:

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"LLM Error : {str(e)}"