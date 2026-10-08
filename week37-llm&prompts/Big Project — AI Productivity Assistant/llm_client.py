import os
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:
    def load_dotenv(*_args, **_kwargs):
        return False

try:
    from google import genai
except ImportError:
    genai = None

ENV_PATH = Path(__file__).resolve().parent / ".env"
load_dotenv(ENV_PATH)

api_key = os.getenv("GEMINI_API_KEY")

if genai is None or not api_key:
    client = None
else:
    client = genai.Client(api_key=api_key)


def ask_llm(prompt):
    if client is None:
        raise RuntimeError(
            "Gemini client is unavailable. Install the 'google-genai' package and set the GEMINI_API_KEY environment variable."
        )

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt,
    )
    if response.text is None:
        raise ValueError("The Gemini response did not include text output.")
    return response.text