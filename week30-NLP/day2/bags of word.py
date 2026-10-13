from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


documents = [
    "I love movies",
    "I love Python",
    "Python is powerful",
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents).toarray()  # type: ignore[attr-defined]

print(vectorizer)
print(X)
print("Vocabulary:")
print(vectorizer.get_feature_names_out())

print("bag of words:")
print(X)

other_documents = [
    "I love this movie",
    "This movie is amazing",
    "I love amazing movies",
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(other_documents).toarray()  # type: ignore[attr-defined]
print("Vocabulary:")
print(vectorizer.get_feature_names_out())

print("\nTF-IDF Matrix:")
print(X)