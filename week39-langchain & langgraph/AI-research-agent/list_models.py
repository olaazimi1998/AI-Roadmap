import requests
from config import GEMINI_API_KEY

url = "https://generativelanguage.googleapis.com/v1beta/models"
r = requests.get(url, params={"key": GEMINI_API_KEY})

for m in r.json().get("models", []):
    if "generateContent" in m["supportedGenerationMethods"]:
        print(m["name"])

        