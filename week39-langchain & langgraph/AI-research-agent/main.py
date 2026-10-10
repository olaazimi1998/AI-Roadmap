from langchain_google_genai import ChatGoogleGenerativeAI
from config import GEMINI_API_KEY  
def main():
    model = ChatGoogleGenerativeAI(
        model="gemini-3.8-flash",
        google_api_key=GEMINI_API_KEY,
        temperature=0
    )
    response = model.invoke(
        "Explain what an AI agent is in three simple sentences."
    )

    print(response.content)


if __name__ == "__main__":

    main()
