import pandas as pd
import ast
import re
from utils import printf
from results_handler import get_random_state

def preprocess_data(dataset_file, num_emails):
    if dataset_file.startswith("enron_clean"):
        dataset_file = f"../datasets/enron_clean/{dataset_file}.csv"

    printf(f"[Preprocessing] Loading dataset: {dataset_file}")
    df = pd.read_csv(dataset_file)
    rs = get_random_state()

    df = df.sample(n=num_emails, random_state=rs)

    df['text'] = df['text'].apply(clean_message_text)

    return df['text']


def clean_message_text(text):
    # Conversion of the (list) string in a real list "["a", "b"]" -> ["a", "b"]
    try:
        text_list = ast.literal_eval(text)
        if not isinstance(text_list, list):
            return ""
    except (ValueError, SyntaxError):
        return text

    # Remove empty strings and spaces
    cleaned_text = " ".join([part.strip() for part in text_list if part.strip()])

    # Remove unwanted non-alphabetic characters (es. punctuation)
    cleaned_text = re.sub(r'[^\w\s]', '', cleaned_text)

    return cleaned_text.strip().lower()


def extract_bodies(emails):
    # Consider only the emails' bodies
    return [email['body'] for email in emails if email['body']]


# def segment_email(text):
#     # ToDo - della suddivisione non funziona un cazzo

#     greeting_pattern = r"^(hello|hi|hey|dear|dood (morning|afternoon|evening)|greetings|to whom it may concern|sir|madam|dear mr\.|dear mrs\.|dear ms\.|dear dr\.|dear [A-Za-z]+),?\s*"
#     closing_pattern = r"(\n|^).*(best regards|kind regards|warm regards|regards|sincerely|yours sincerely|yours faithfully|thank you|thanks|cheers|take care|with appreciation|respectfully|with gratitude|yours truly),?\s*$"

#     greeting = re.search(greeting_pattern, text, flags=re.IGNORECASE)
#     closing = re.search(closing_pattern, text, flags=re.IGNORECASE)

#     # Extraction of identified parts
#     greeting = greeting.group(0).strip() if greeting else ""
#     closing = closing.group(0).strip() if closing else ""
#     body = re.sub(f"{greeting_pattern}|{closing_pattern}", "", text).strip()

#     return {
#         "greeting": greeting,
#         "body": body,
#         "closing": closing
#     }


# def stopword_removal(tokens):
#     stopwords = ['of', 'on', 'i', 'am', 'this', 'is', 'a', 'was']
#     filtered_tokens = []
#     for token in tokens:
#         if token not in stopwords:
#             filtered_tokens.append(token)
#     return filtered_tokens


# def stemming(filtered_tokens):
#     root_to_token = {'you have': ['youve'],
#                      'select': ['selected', 'selection'],
#                      'it is': ['its'],
#                      'move': ['moving'],
#                      'photo': ['photos'],
#                      'success': ['successfully', 'successful']
#                      }
#
#     base_form_tokens = []
#     for token in filtered_tokens:
#         for base_form, token_list in root_to_token.items():
#             if token in token_list:
#                 base_form_tokens.append(base_form)
#             else:
#                 base_form_tokens.append(token)
#     return base_form_tokens


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
