import chromadb
from sentence_transformers import SentenceTransformer
from torch import embedding

model = SentenceTransformer(
"sentence-transformers/all-MiniLM-L6-v2"
)
client = chromadb.PersistentClient(
    path="./week40-vector database/demo_chromadb_db"
)

collection = client.get_or_create_collection(
    name="learning_documents"
)

documents = [
    "Python is a popular programming language for AI.",
    "Machine learning allows computers to learn from data.",
    "Docker packages applications into containers.",
    "Vector databases store and search embeddings.",
    "FastAPI helps developers build Python APIs."
]
embeddings  = model.encode(documents).tolist()

collection.upsert(
    ids=["doc1", "doc2", "doc3", "doc4", "doc5"],
    documents=documents,
    embeddings=embeddings
)
query = "how can i find similar text using embedding?"

query_embedding = model.encode(query).tolist()

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)
print("\nQuestion:")
print(query)

print("\nSearch results:")
for document, distance in zip(
    results["documents"][0], # type: ignore
    results["distances"][0]
):
    print(f"\nDocument: {document}")
    print(f"Distance: {distance:.4f}")



print("Documents stored successfully!")

print("Number of stored documents:", collection.count())