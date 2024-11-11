import pandas as pd
import re

def preprocess_data(dataset_file, num_emails, random_selection):
    # Dataset loading 
    df = pd.read_csv(dataset_file)

    # Select emails, randomly or sorted
    if random_selection:
        df = df.sample(n=num_emails, random_state=42)
    else:
        df = df.head(num_emails)
    
    # Email text extraction
    emails = df['message'].apply(clean_email_text)
    return emails

def clean_email_text(text):
    # Removing emails' metadata and normalization
    cleaned_text = re.sub(r"Message-ID:.*|Date:.*|From:.*|To:.*|Subject:.*|X-.*:.*", "", text)
    return cleaned_text.strip()

