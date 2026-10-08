import os

try:
    from dotenv import load_dotenv
except ImportError:
    def load_dotenv(*_args, **_kwargs):
        return False

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

load_dotenv()

if OpenAI is None:
    client = None
else:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ask_llm(prompt):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
    )

    return response.output_text