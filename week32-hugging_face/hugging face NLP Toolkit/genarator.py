from transformers import pipeline


def generate_text(prompt):
    generator = pipeline("text-generation")

    result = generator(
        prompt,
        max_new_tokens=50,
        num_return_sequences=1
    )

    return result[0]["generated_text"]


if __name__ == "__main__":
    prompt = input("Enter your prompt: ")

    result = generate_text(prompt)

    print("\nGenerated text:")
    print(result)