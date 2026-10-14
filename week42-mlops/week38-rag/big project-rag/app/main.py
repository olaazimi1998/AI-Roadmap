from pathlib import Path

from app.loader import load_pdf
from app.chunker import split_into_chunks
from app.vector_store import VectorStore


def resolve_pdf_path(pdf_path: str | Path | None = None) -> Path:
    if pdf_path is not None:
        return Path(pdf_path)

    project_root = Path(__file__).resolve().parents[1]
    candidates = [
        project_root / "documents" / "examples.pdf",
        project_root / "documents" / "example.pdf",
    ]

    for candidate in candidates:
        if candidate.exists():
            return candidate

    return candidates[0]


def main(pdf_path: str | Path | None = None):
    pdf_path = resolve_pdf_path(pdf_path)

    # Step 1: Load the PDF
    document_text = load_pdf(str(pdf_path))

    if not document_text.strip():
        print("No extractable text was found in the PDF.")
        return

    # Step 2: Split the text into chunks
    chunks = split_into_chunks(document_text)

    print(f"Created {len(chunks)} chunks.")

    # Step 3: Create the vector store
    vector_store = VectorStore()
    vector_store.add_documents(chunks)

    # Step 4: Ask questions
    print("\nPDF Question Answering")
    print("Type 'exit' to stop.")

    while True:
        question = input("\nYour question: ").strip()

        if question.lower() == "exit":
            break

        if not question:
            print("Please enter a question.")
            continue

        # Step 5: Retrieve relevant chunks
        relevant_chunks = vector_store.search(
            question,
            top_k=3
        )

        # Step 6: Display the retrieved information
        print("\nRelevant information:")

        for number, chunk in enumerate(relevant_chunks, start=1):
            print(f"\n--- Chunk {number} ---")
            print(chunk)


if __name__ == "__main__":
    main()
    #cd "C:\Users\olaaz\Documents\AI Roadmap\week38-rag\big project-rag"; .\.venv\Scripts\python.exe -m pytest -q