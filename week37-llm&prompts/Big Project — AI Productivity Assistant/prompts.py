def summary_prompt(text):
    return f"""
You are an expert summarization assistant.

Summarize the following text clearly and briefly.

Text:
{text}

Requirements:
- Keep the important information.
- Remove unnecessary details.
- Use simple English.
"""


def sentiment_prompt(text):
    return f"""
You are a sentiment analysis assistant.

Analyze the sentiment of the following text.

Text:
{text}

Return:
- Sentiment: Positive, Negative, or Neutral
- Reason: one short explanation
"""


def translation_prompt(text, language):
    return f"""
You are a professional translator.

Translate the following text into {language}.

Text:
{text}

Requirements:
- Keep the original meaning.
- Use natural language.
- Do not add extra information.
"""


def extraction_prompt(text):
    return f"""
You are an information extraction assistant.

Extract useful information from the text below.

Text:
{text}

Return:
- Name
- Email
- Phone
- Organization

If something is not available, write "Not found".
"""


def code_prompt(description):
    return f"""
You are an expert Python programmer.

Write Python code for the following task:

{description}

Requirements:
- Use clean Python.
- Keep the code easy to understand.
- Add short comments where useful.
- Return only the code and a short explanation.
"""