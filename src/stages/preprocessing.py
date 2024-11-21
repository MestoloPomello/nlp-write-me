import pandas as pd
import re
from results_handler import get_random_state
from utils import printf


def preprocess_data(dataset_file, num_emails):
    # Dataset loading
    printf(f"[Preprocessing] Loading dataset: {dataset_file}")
    df = pd.read_csv(dataset_file)
    df = df.sample(n=num_emails, random_state=get_random_state())

    # Email text extraction
    emails = df['message'].apply(clean_email_text)
    emails = df['message'].apply(segment_email)

    # append_to_results("\n".join(emails))  # Temp removed emails output

    return emails


# def clean_email_text_OLD(text):
#     # Removing emails' metadata and normalization
#     regexes = [
#         r"Message-ID:.*",
#         r"Date:.*",
#         r"From:.*",
#         r"To:.*",
#         r"Subject:.*",
#         r"X-.*:.*",
#         r"Mime-Version:.*",
#         r"Content-.*:.*"
#     ]
#     regexStr = "|".join(regexes)
#     cleaned_text = re.sub(regexStr, "", text)
#     return cleaned_text.strip().lower()


def clean_email_text(text):
    parts = text.split("\n\n", 1)

    if len(parts) > 1:
        header, body = parts
    else:
        body = text

    # print(body)

    return body.strip().lower()


def segment_email(text):
    # Pattern per identificare le sezioni

    # ToDo - della suddivisione non funziona un cazzo

    greeting_pattern = r"^(Hello|Hi|Hey|Dear|Good (morning|afternoon|evening)|Greetings|To whom it may concern|Sir|Madam|Dear Mr\.|Dear Mrs\.|Dear Ms\.|Dear Dr\.|Dear [A-Za-z]+),?\s*"
    closing_pattern = r"(\n|^).*(Best regards|Kind regards|Warm regards|Regards|Sincerely|Yours sincerely|Yours faithfully|Thank you|Thanks|Cheers|Take care|With appreciation|Respectfully|With gratitude|Yours truly),?\s*$"

    greeting = re.search(greeting_pattern, text, flags=re.IGNORECASE)
    closing = re.search(closing_pattern, text, flags=re.IGNORECASE)

    # Estrai le parti identificate
    greeting = greeting.group(0).strip() if greeting else ""
    closing = closing.group(0).strip() if closing else ""
    body = re.sub(f"{greeting_pattern}|{closing_pattern}", "", text).strip()

    return {
        "greeting": greeting,
        "body": body,
        "closing": closing
    }
