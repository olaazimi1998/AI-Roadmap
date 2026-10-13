import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


class VectorStore:
    def __init__(self):
        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

        self.index = None
        self.chunks = []

    def add_documents(self, chunks: list[str]) -> None:
        if not chunks:
            raise ValueError("No chunks were provided.")

        self.chunks = chunks

        embeddings = self.model.encode(
            chunks,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        embeddings = np.asarray(embeddings, dtype="float32")

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatIP(dimension)
        self.index.add(embeddings)

    def search(self, question: str, top_k: int = 3) -> list[str]:
        if self.index is None:
            raise RuntimeError("Add documents before searching.")

        if top_k <= 0:
            raise ValueError("top_k must be positive.")

        normalized_question = (question or "").strip()
        if not normalized_question:
            raise ValueError("Question must not be blank.")

        query_embedding = self.model.encode(
            [normalized_question],
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        query_embedding = np.asarray(
            query_embedding,
            dtype="float32"
        )

        k = min(top_k, len(self.chunks))

        scores, indices = self.index.search(query_embedding, k)

        results = []

        for index in indices[0]:
            if index >= 0:
                results.append(self.chunks[index])

        return results