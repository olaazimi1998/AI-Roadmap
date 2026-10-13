from llm_client import ask_llm

from prompts import (
    summary_prompt,
    sentiment_prompt,
    translation_prompt,
    extraction_prompt,
    code_prompt
)


def summarize(text):
    prompt = summary_prompt(text)
    return ask_llm(prompt)


def analyze_sentiment(text):
    prompt = sentiment_prompt(text)
    return ask_llm(prompt)


def translate(text, language):
    prompt = translation_prompt(text, language)
    return ask_llm(prompt)


def extract_information(text):
    prompt = extraction_prompt(text)
    return ask_llm(prompt)


def generate_code(description):
    prompt = code_prompt(description)
    return ask_llm(prompt)