from tasks import (
    summarize,
    analyze_sentiment,
    translate,
    extract_information,
    generate_code
)


def show_menu():
    print("\n==============================")
    print("   AI Productivity Assistant")
    print("==============================")

    print("1. Summarize text")
    print("2. Analyze sentiment")
    print("3. Translate text")
    print("4. Extract information")
    print("5. Generate Python code")
    print("0. Exit")


def main():

    while True:

        show_menu()

        choice = input("\nChoose a task: ")

        if choice == "1":

            text = input("\nEnter text:\n")

            result = summarize(text)

            print("\n--- Summary ---")
            print(result)

        elif choice == "2":

            text = input("\nEnter text:\n")

            result = analyze_sentiment(text)

            print("\n--- Sentiment ---")
            print(result)

        elif choice == "3":

            text = input("\nEnter text:\n")
            language = input("Translate to which language? ")

            result = translate(text, language)

            print("\n--- Translation ---")
            print(result)

        elif choice == "4":

            text = input("\nEnter text:\n")

            result = extract_information(text)

            print("\n--- Extracted Information ---")
            print(result)

        elif choice == "5":

            description = input(
                "\nDescribe the Python program you need:\n"
            )

            result = generate_code(description)

            print("\n--- Generated Code ---")
            print(result)

        elif choice == "0":

            print("\nGoodbye!")
            break

        else:

            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()