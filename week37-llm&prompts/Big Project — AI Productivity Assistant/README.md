# AI Productivity Assistant

This project provides a lightweight AI assistant for summarizing text, analyzing sentiment, translating text, extracting information, and generating Python code.

## Run the CLI

```bash
python main.py
```

## Run the FastAPI app

Install dependencies:

```bash
pip install -r requirements.txt
```

Then start the API:

```bash
python main.py --api
```

The API will be available at http://localhost:8000 and the interactive docs will be available at http://localhost:8000/docs.

## Supported API endpoints

- `GET /health`
- `POST /summarize`
- `POST /analyze-sentiment`
- `POST /translate`
- `POST /extract-information`
- `POST /generate-code`
