from transformers import pipeline


def answer_question(question, context):
    qa = pipeline("question-answering")

    result = qa(
        question=question,
        context=context
    )

    return result


if __name__ == "__main__":

    context = """
    Python is a programming language created by Guido van Rossum.
    Python was first released in 1991.
    Python is widely used in data science, machine learning,
    web development, and artificial intelligence.
    """

    question = input("Ask a question: ")

    result = answer_question(question, context)

    print("\nAnswer:", result["answer"])
    print("Confidence:", result["score"])