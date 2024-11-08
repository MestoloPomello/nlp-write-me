import pandas as pd
import re

def preprocess_data(dataset_file, num_emails):
    # Caricamento del dataset
    df = pd.read_csv(dataset_file)
    df = df.head(num_emails)
    
    # Estrazione del testo delle email
    emails = df['message'].apply(clean_email_text)
    return emails

def clean_email_text(text):
    # Rimozione dei metadati delle email e normalizzazione
    cleaned_text = re.sub(r"Message-ID:.*|Date:.*|From:.*|To:.*|Subject:.*|X-.*:.*", "", text)
    return cleaned_text.strip()

