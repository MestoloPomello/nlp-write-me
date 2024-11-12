import pandas as pd
import re
import random
from results_handler import append_to_results

def preprocess_data(dataset_file, num_emails, random_selection):
    # Dataset loading 
    print(f"[Preprocessing] Loading dataset: {dataset_file}")
    df = pd.read_csv(dataset_file)

    # Select emails, randomly or sorted
    if random_selection:
        random_state = random.randint(1, 10000)
        df = df.sample(n=num_emails, random_state=random_state)
    else:
        df = df.head(num_emails)

    append_to_results(f"Random State: {random_state}")
    
    # Email text extraction
    emails = df['message'].apply(clean_email_text)
    # print(f"[Preprocessing] Cleaned emails: \n{"\n".join(emails)}")

    append_to_results("\n".join(emails))

    return emails

def clean_email_text(text):
    # Removing emails' metadata and normalization
    cleaned_text = re.sub(r"Message-ID:.*|Date:.*|From:.*|To:.*|Subject:.*|X-.*:.*|Mime-Version:.*|Content-.*:.*", "", text)
    return cleaned_text.strip()

