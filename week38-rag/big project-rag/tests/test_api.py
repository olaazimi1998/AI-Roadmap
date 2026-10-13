from fastapi.testclient import TestClient

from app import api


class FakeVectorStore:
    def add_documents(self, chunks: list[str]) -> None:
        self.chunks = chunks

    def search(self, question: str, top_k: int = 3) -> list[str]:
        return self.chunks[:top_k]


def test_upload_and_search_document(monkeypatch):
    monkeypatch.setattr(api, "VectorStore", FakeVectorStore)
    monkeypatch.setattr(
        api,
        "load_pdf_bytes",
        lambda content: "RAG retrieves relevant passages from a document.",
    )
    api.app.state.retrieval_service = api.RetrievalService()

    with TestClient(api.app) as client:
        upload_response = client.post(
            "/documents",
            files={"file": ("guide.pdf", b"%PDF-1.4 content", "application/pdf")},
        )

        assert upload_response.status_code == 201
        assert upload_response.json()["chunks"] == 1

        answer_response = client.post(
            "/ask",
            json={"question": "What does RAG retrieve?", "top_k": 1},
        )

    assert answer_response.status_code == 200
    assert answer_response.json()["results"] == [
        {
            "rank": 1,
            "text": "RAG retrieves relevant passages from a document.",
        }
    ]


def test_upload_rejects_non_pdf():
    api.app.state.retrieval_service = api.RetrievalService()

    with TestClient(api.app) as client:
        response = client.post(
            "/documents",
            files={"file": ("notes.txt", b"not a PDF", "text/plain")},
        )

    assert response.status_code == 400


def test_ask_indexes_the_sample_pdf_by_default(monkeypatch):
    monkeypatch.setattr(api, "VectorStore", FakeVectorStore)
    monkeypatch.setattr(api, "load_pdf", lambda path: "A sample PDF passage.")
    api.app.state.retrieval_service = api.RetrievalService()

    with TestClient(api.app) as client:
        response = client.post(
            "/ask",
            json={"question": "What is in the sample?"},
        )

    assert response.status_code == 200
    assert response.json()["results"][0]["text"] == "A sample PDF passage."
