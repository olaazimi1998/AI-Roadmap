from classifier import analyze_sentiment
from genarator import generate_text
from question_answering import answer_question


def show_menu():
    print("\n==============================")
    print("      AI NLP TOOLKIT")
    print("==============================")
    print("1. Sentiment Analysis")
    print("2. Text Generation")
    print("3. Question Answering")
    print("4. Exit")
    print("==============================")


def sentiment_app():
    text = input("\nEnter text: ")

    result = analyze_sentiment(text)

    print("\nResult:")
    print("Sentiment:", result["label"])
    print("Confidence:", result["score"])


def generator_app():
    prompt = input("\nEnter your prompt: ")

    result = generate_text(prompt)

    print("\nGenerated text:")
    print(result)


def qa_app():
    context = input("\nEnter the context: ")
    question = input("Enter your question: ")

    result = answer_question(question, context)

    print("\nAnswer:", result["answer"])
    print("Confidence:", result["score"])


while True:

    show_menu()

    choice = input("Choose an option: ")

    if choice == "1":
        sentiment_app()

    elif choice == "2":
        generator_app()

    elif choice == "3":
        qa_app()

    elif choice == "4":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice.")