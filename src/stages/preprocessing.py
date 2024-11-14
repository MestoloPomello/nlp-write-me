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

    # append_to_results("\n".join(emails))  # Temp removed emails output

    return emails


def clean_email_text(text):
    # Removing emails' metadata and normalization
    regexes = [
        r"Message-ID:.*",
        r"Date:.*",
        r"From:.*",
        r"To:.*",
        r"Subject:.*",
        r"X-.*:.*",
        r"Mime-Version:.*",
        r"Content-.*:.*"
    ]
    regexStr = "|".join(regexes)
    cleaned_text = re.sub(regexStr, "", text)
    return cleaned_text.strip().lower()
