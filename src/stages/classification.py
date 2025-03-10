import re
import pandas as pd
from results_handler import full_output, append_to_processed_emails

greeting_pattern = r"^(hello|my name is|i am|hi|hey|dear|good (morning|afternoon|evening)|greetings|to whom it may concern|sir|madam|dear mr\.|dear mrs\.|dear ms\.|dear dr\.|dear [A-Za-z]+).*$"
closing_pattern = r"(\n|^).*(best regards|kind regards|sincerely|thank you|thanks|cheers|yours truly|take care|with appreciation|respectfully|with gratitude|yours faithfully),?\s*$"


def classify_email_dataset(text):
    classified_emails = text.apply(classify_email_parts)

    # Convert the dict in a DataFrame while only keeping the non-empty strings
    classified_text = pd.DataFrame(classified_emails.tolist())

    # Append every processed email to the file
    for _, row in classified_text.iterrows():
        append_to_processed_emails(row)
    
    # Full output for the 3 lists (greetings, bodies and closings)
    full_output(
        "Classification",
        "Email parts were saved to the processed_emails.csv file in the evaluation folder.",
        newline=True
    )

    return classified_text


def classify_email_parts(text):
    text = text.strip()

    greeting_match = re.search(greeting_pattern, text, flags=re.IGNORECASE | re.MULTILINE)
    greeting = greeting_match.group(0).strip() if greeting_match else ""

    closing_match = re.search(closing_pattern, text, flags=re.IGNORECASE | re.MULTILINE)
    closing = closing_match.group(0).strip() if closing_match else ""

    # Remove greeting and closing from the email body
    body = text
    if greeting:
        body = body.replace(greeting, "", 1).strip()
    if closing:
        body = body.replace(closing, "", 1).strip()

    body_sentences = split_sentences(body)

    results = {
        "greeting": greeting,
        "body": body_sentences,
        "closing": closing
    }

    return results


def split_sentences(text):
    # Replace multiple newlines with a single newline to avoid issues
    text = re.sub(r'\n+', '\n', text).strip()

    sentences = []
    buffer = ""

    for char in text:
        buffer += char
        if char == "\n" or char == ".":
            sentences.append(buffer.strip())
            buffer = ""

    # Add the last sentence (if present)
    if buffer.strip():
        sentences.append(buffer.strip())

    return sentences
