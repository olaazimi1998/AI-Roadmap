from io import BytesIO
from pathlib import Path

from pypdf import PdfReader
from pypdf.errors import PdfReadError


def load_pdf(file_path: str) -> str:
    """Extract text from a PDF file."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {file_path}")

    return load_pdf_bytes(path.read_bytes())


def load_pdf_bytes(content: bytes) -> str:
    """Extract text from PDF content held in memory."""
    if not content:
        return ""

    try:
        reader = PdfReader(BytesIO(content))
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    except Exception as exc:  # pypdf raises several parse-related exceptions
        raise ValueError("The uploaded file is not a readable PDF.") from exc

