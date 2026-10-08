import sys

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from tasks import (
    summarize,
    analyze_sentiment,
    translate,
    extract_information,
    generate_code,
)


class TextRequest(BaseModel):
    text: str = Field(..., min_length=1)


class TranslationRequest(BaseModel):
    text: str = Field(..., min_length=1)
    language: str = Field(..., min_length=1)


class CodeRequest(BaseModel):
    description: str = Field(..., min_length=1)


app = FastAPI(
    title="AI Productivity Assistant",
    description="API for summarizing text, analyzing sentiment, translating text, extracting information, and generating Python code.",
    version="1.0.0",
)


def _run_task(task_name, task_func, *args):
    try:
        return task_func(*args)
    except RuntimeError as exc:
        raise HTTPException(
            status_code=503,
            detail=f"{task_name} is unavailable: {exc}",
        ) from exc
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=f"{task_name} could not process the input: {exc}",
        ) from exc


@app.get("/", tags=["meta"])
async def root():
    return {
        "service": "AI Productivity Assistant",
        "message": "Use /docs for the interactive API documentation.",
        "endpoints": [
            "/health",
            "/summarize",
            "/analyze-sentiment",
            "/translate",
            "/extract-information",
            "/generate-code",
        ],
    }


@app.get("/health", tags=["meta"])
async def health_check():
    return {"status": "ok", "service": "AI Productivity Assistant"}


@app.post("/summarize", tags=["ai"])
async def summarize_endpoint(request: TextRequest):
    return {"input": request.text, "result": _run_task("summarize", summarize, request.text)}


@app.post("/analyze-sentiment", tags=["ai"])
async def analyze_sentiment_endpoint(request: TextRequest):
    return {"input": request.text, "result": _run_task("analyze_sentiment", analyze_sentiment, request.text)}


@app.post("/translate", tags=["ai"])
async def translate_endpoint(request: TranslationRequest):
    return {
        "input": request.text,
        "language": request.language,
        "result": _run_task("translate", translate, request.text, request.language),
    }


@app.post("/extract-information", tags=["ai"])
async def extract_information_endpoint(request: TextRequest):
    return {"input": request.text, "result": _run_task("extract_information", extract_information, request.text)}


@app.post("/generate-code", tags=["ai"])
async def generate_code_endpoint(request: CodeRequest):
    return {"description": request.description, "result": _run_task("generate_code", generate_code, request.description)}


def show_menu():
    print("\n==============================")
    print("   AI Productivity Assistant")
    print("==============================")

    print("1. Summarize text")
    print("2. Analyze sentiment")
    print("3. Translate text")
    print("4. Extract information")
    print("5. Generate Python code")
    print("0. Exit")


def run_cli():
    while True:
        show_menu()

        choice = input("\nChoose a task: ")

        if choice == "1":
            text = input("\nEnter text:\n")
            result = summarize(text)
            print("\n--- Summary ---")
            print(result)

        elif choice == "2":
            text = input("\nEnter text:\n")
            result = analyze_sentiment(text)
            print("\n--- Sentiment ---")
            print(result)

        elif choice == "3":
            text = input("\nEnter text:\n")
            language = input("Translate to which language? ")
            result = translate(text, language)
            print("\n--- Translation ---")
            print(result)

        elif choice == "4":
            text = input("\nEnter text:\n")
            result = extract_information(text)
            print("\n--- Extracted Information ---")
            print(result)

        elif choice == "5":
            description = input("\nDescribe the Python program you need:\n")
            result = generate_code(description)
            print("\n--- Generated Code ---")
            print(result)

        elif choice == "0":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.")


def main():
    if "--api" in sys.argv:
        import uvicorn

        uvicorn.run(app, host="0.0.0.0", port=8000)
        return

    run_cli()


if __name__ == "__main__":
    main()