import pandas as pd
import re
from results_handler import append_to_results, get_random_state

def preprocess_data(dataset_file, num_emails):
    # Dataset loading 
    print(f"[Preprocessing] Loading dataset: {dataset_file}")
    df = pd.read_csv(dataset_file)

    df = df.sample(n=num_emails, random_state=get_random_state())

    # Email text extraction
    emails = df['message'].apply(clean_email_text)
    # print(f"[Preprocessing] Cleaned emails: \n{"\n".join(emails)}")

    append_to_results("\n".join(emails))

    return emails

def clean_email_text(text):
    # Removing emails' metadata and normalization
    cleaned_text = re.sub(r"Message-ID:.*|Date:.*|From:.*|To:.*|Subject:.*|X-.*:.*|Mime-Version:.*|Content-.*:.*", "", text)
    return cleaned_text.strip()

