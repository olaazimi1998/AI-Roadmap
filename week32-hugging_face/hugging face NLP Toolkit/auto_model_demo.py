from transformers import AutoTokenizer, AutoModel


model_name = "bert-base-uncased"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModel.from_pretrained(model_name)

text = "I am learning AI engineering."

tokens = tokenizer(
    text,
    return_tensors="pt"
)

print("Tokens:")
print(tokens)

print("\nModel loaded successfully!")

print("Model type:")
print(model.__class__.__name__)