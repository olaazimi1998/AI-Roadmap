import logging
from pathlib import Path

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.concurrency import run_in_threadpool
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel, Field

from tasks import (
    analyze_sentiment,
    extract_information,
    generate_code,
    summarize,
    translate,
)

logger = logging.getLogger(__name__)
MAX_UPLOAD_BYTES = 1_000_000
SUPPORTED_FILE_TYPES = {".txt", ".md", ".csv"}
FRONTEND_PATH = Path(__file__).resolve().parent / "static" / "index.html"

TASKS = {
    "summarize": summarize,
    "analyze-sentiment": analyze_sentiment,
    "translate": translate,
    "extract-information": extract_information,
    "generate-code": generate_code,
}

app = FastAPI(
    title="AI Productivity Assistant",
    description="Summarize, analyze sentiment, translate, extract information, and generate code.",
    version="1.0.0",
)


class TextRequest(BaseModel):
    text: str = Field(..., min_length=1)


class TranslationRequest(TextRequest):
    language: str = Field(..., min_length=1)


class CodeRequest(BaseModel):
    description: str = Field(..., min_length=1)


def _model_info():
    return {"provider": "gemini", "model": "gemini-3.8-flash"}


def _response(task_name, result, **metadata):
    return {
        "success": True,
        "task": task_name,
        **_model_info(),
        "result": result,
        **metadata,
    }


def _run_task(task_name, function, *args):
    try:
        result = function(*args)
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
    return _response(task_name, result)


@app.exception_handler(HTTPException)
async def http_error_handler(_, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"success": False, "error": exc.detail},
        headers=exc.headers,
    )


@app.exception_handler(RequestValidationError)
async def validation_error_handler(_, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "error": "Invalid request",
            "details": jsonable_encoder(exc.errors()),
        },
    )


@app.exception_handler(Exception)
async def unexpected_error_handler(_, exc: Exception):
    logger.exception("Unhandled API error", exc_info=exc)
    return JSONResponse(
        status_code=500,
        content={"success": False, "error": "Internal server error."},
    )


@app.get("/", tags=["meta"])
def home():
    if not FRONTEND_PATH.is_file():
        raise HTTPException(
            status_code=404,
            detail="Frontend file is missing from the static directory.",
        )
    return FileResponse(FRONTEND_PATH, media_type="text/html")


@app.get("/health", tags=["meta"])
def health():
    return {"success": True, "status": "ok", **_model_info()}


@app.post("/summarize", tags=["ai"])
def summarize_text(request: TextRequest):
    return _run_task("summarize", summarize, request.text)


@app.post("/analyze-sentiment", tags=["ai"])
def analyze_text_sentiment(request: TextRequest):
    return _run_task("analyze-sentiment", analyze_sentiment, request.text)


@app.post("/translate", tags=["ai"])
def translate_text(request: TranslationRequest):
    return _run_task("translate", translate, request.text, request.language)


@app.post("/extract-information", tags=["ai"])
def extract_text_information(request: TextRequest):
    return _run_task("extract-information", extract_information, request.text)


@app.post("/generate-code", tags=["ai"])
def generate_python_code(request: CodeRequest):
    return _run_task("generate-code", generate_code, request.description)


@app.post("/upload/{task_name}", tags=["ai"])
async def process_uploaded_file(
    task_name: str,
    file: UploadFile = File(...),
    language: str = Form(""),
):
    function = TASKS.get(task_name)
    if function is None:
        await file.close()
        raise HTTPException(status_code=404, detail="Unknown AI task.")

    filename = Path(file.filename or "")
    if filename.suffix.lower() not in SUPPORTED_FILE_TYPES:
        await file.close()
        raise HTTPException(
            status_code=415,
            detail="Upload a .txt, .md, or .csv text file.",
        )

    content = await file.read(MAX_UPLOAD_BYTES + 1)
    await file.close()
    if len(content) > MAX_UPLOAD_BYTES:
        raise HTTPException(
            status_code=413,
            detail=f"File is too large. Maximum size is {MAX_UPLOAD_BYTES} bytes.",
        )
    try:
        text = content.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise HTTPException(
            status_code=400,
            detail="The uploaded file must use UTF-8 text encoding.",
        ) from exc
    if not text.strip():
        raise HTTPException(status_code=400, detail="The uploaded file is empty.")
    if task_name == "translate" and not language.strip():
        raise HTTPException(
            status_code=422,
            detail="The language field is required for translation.",
        )

    args = (text, language) if task_name == "translate" else (text,)
    response = await run_in_threadpool(_run_task, task_name, function, *args)
    response["filename"] = filename.name
    return response
