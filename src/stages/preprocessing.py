import pandas as pd
import re
from utils import printf
from results_handler import get_random_state


def preprocess_data(dataset_file, num_emails):
    if dataset_file.startswith("fraud"):
        dataset_file = f"../datasets/fraudulent/Nigerian_Fraud.csv"

    printf(f"[Preprocessing] Loading dataset: {dataset_file}")
    df = pd.read_csv(dataset_file)
    rs = get_random_state()

    # If num_emails is greater than the total number of emails (or is -1), keep the whole dataset
    if num_emails > len(df) or num_emails == -1:
        num_emails = len(df)
    else:
        df = df.sample(n=num_emails, random_state=rs)

    df['body'] = df['body'].apply(clean_message_text)

    return df


def clean_message_text(text):
    cleaned_text = text.strip()
    cleaned_text = re.sub(r"[^\w\s.]", "", cleaned_text)
    return cleaned_text.strip().lower()