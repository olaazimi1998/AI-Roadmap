from sentence_transformers import SentenceTransformer
from torch import embedding

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)
sentence = "Python is useful for artificial intellegence"
embedding = model.encode(sentence)

print("Orignal sentence and embedding")
print(sentence)
print(embedding.shape)
print(embedding[:5])