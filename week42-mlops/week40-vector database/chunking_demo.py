def split_text(text, chunk_size=100):
    """Split text into simple character-based chunks."""
    chunks = []

    for start in range(0, len(text), chunk_size):
        chunk = text[start:start + chunk_size]
        chunks.append(chunk)

    return chunks


text = """
Vector databases store and search embeddings.
Sentence Transformers creates embeddings from text.
ChromaDB helps retrieve similar documents.
"""

chunks = split_text(text, chunk_size=50)

for index, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {index}:")
    print(chunk)