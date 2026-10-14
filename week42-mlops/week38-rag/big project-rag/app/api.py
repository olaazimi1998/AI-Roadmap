from pathlib import Path

from fastapi import FastAPI, File, HTTPException, Request, UploadFile, status
from pydantic import BaseModel, Field

from app.chunker import split_into_chunks
from app.loader import load_pdf, load_pdf_bytes
from app.vector_store import VectorStore


DEFAULT_PDF_PATH = (
    Path(__file__).resolve().parents[1] / "documents" / "examples.pdf"
)


class QuestionRequest(BaseModel):
    question: str = Field(min_length=1, max_length=2000)
    top_k: int = Field(default=3, ge=1, le=20)


class SearchResult(BaseModel):
    rank: int
    text: str


class QuestionResponse(BaseModel):
    question: str
    results: list[SearchResult]


class DocumentResponse(BaseModel):
    message: str
    chunks: int


class RetrievalService:
    def __init__(self, default_pdf_path: Path = DEFAULT_PDF_PATH):
        self.default_pdf_path = default_pdf_path
        self.vector_store: VectorStore | None = None
        self.chunk_count = 0

    @property
    def is_indexed(self) -> bool:
        return self.vector_store is not None

    def index_text(self, text: str) -> int:
        if not text.strip():
            raise ValueError("The PDF contains no extractable text.")

        chunks = split_into_chunks(text)
        if not chunks:
            raise ValueError("The PDF contains no indexable text.")

        vector_store = VectorStore()
        vector_store.add_documents(chunks)
        self.vector_store = vector_store
        self.chunk_count = len(chunks)
        return self.chunk_count

    def index_pdf(self, content: bytes) -> int:
        return self.index_text(load_pdf_bytes(content))

    def ensure_default_document(self) -> None:
        if self.is_indexed:
            return

        if not self.default_pdf_path.exists():
            raise FileNotFoundError(
                f"Default PDF not found: {self.default_pdf_path}"
            )

        self.index_text(load_pdf(str(self.default_pdf_path)))

    def search(self, question: str, top_k: int) -> list[str]:
        self.ensure_default_document()
        if self.vector_store is None:
            raise RuntimeError("The document index was not initialized.")
        return self.vector_store.search(question, top_k=top_k)


app = FastAPI(
    title="PDF Question Answering API",
    description="Upload a PDF and retrieve the passages most relevant to a question.",
    version="1.0.0",
)
app.state.retrieval_service = RetrievalService()


def get_service(request: Request) -> RetrievalService:
    return request.app.state.retrieval_service


@app.get("/health")
def health(request: Request) -> dict[str, str | bool | int]:
    service = get_service(request)
    return {
        "status": "ok",
        "document_loaded": service.is_indexed,
        "chunks": service.chunk_count,
    }


@app.post(
    "/documents",
    response_model=DocumentResponse,
    status_code=status.HTTP_201_CREATED,
)
def upload_document(
    request: Request,
    file: UploadFile = File(...),
) -> DocumentResponse:
    if not file.filename or Path(file.filename).suffix.lower() != ".pdf":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Upload a file with a .pdf extension.",
        )

    content = file.file.read()
    if not content.startswith(b"%PDF-"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The uploaded file is not a valid PDF.",
        )

    try:
        chunk_count = get_service(request).index_pdf(content)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc

    return DocumentResponse(
        message="PDF indexed successfully.",
        chunks=chunk_count,
    )


@app.post("/ask", response_model=QuestionResponse)
def ask_question(
    body: QuestionRequest,
    request: Request,
) -> QuestionResponse:
    question = body.question.strip()
    if not question:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Question must not be blank.",
        )

    try:
        results = get_service(request).search(question, body.top_k)
    except FileNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(exc),
        ) from exc
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(exc),
        ) from exc

    return QuestionResponse(
        question=question,
        results=[
            SearchResult(rank=rank, text=text)
            for rank, text in enumerate(results, start=1)
        ],
    )
