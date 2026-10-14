# PDF Question Answering API

## Overview

A beginner-friendly retrieval augmented generation (RAG) project. It extracts
text from a PDF, splits it into chunks, embeds the chunks, and uses FAISS to
retrieve passages relevant to a question.

## Features

- Extract text from PDF files
- Split text into chunks
- Generate text embeddings
- Search for relevant chunks
- Upload PDFs and ask questions through a FastAPI service

## Technologies

- Python
- FastAPI and Uvicorn
- pypdf
- Sentence Transformers
- FAISS
- NumPy

## Setup

From this project directory, create and activate a virtual environment, then
install the dependencies:

```bash
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Start the API:

```bash
uvicorn app.api:app --reload
```

Open <http://127.0.0.1:8000/docs> to try the interactive API documentation.

## API

- `GET /health` reports whether a PDF has been indexed.
- `POST /documents` accepts a PDF upload as multipart form data with the field
  name `file`. Uploading another PDF replaces the current in-memory index.
- `POST /ask` accepts JSON such as
  `{"question": "What is retrieval augmented generation?", "top_k": 3}` and
  returns the most relevant passages.

If no PDF has been uploaded, the first question indexes
`documents/examples.pdf`. The API returns retrieved passages; it does not
generate a new answer with a language model.
