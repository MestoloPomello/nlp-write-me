import pandas as pd
import re


def clean_email_text(text):
    # Splitting text between header and body
    parts = text.split("\n\n", 1)

    if len(parts) > 1:
        _, body = parts
    else:
        body = text

    body = punctuation_removal(body)

    return body.strip().lower()


def punctuation_removal(text):
    return re.sub(r'[^\w\s]', '', text)


def process_and_save_emails(dataset_file, output_file, chunksize=1000):
    print("Starting email processing...")

    # Creation of input file with headers
    with open(output_file, "w") as f:
        f.write("file,cleaned_message\n")  # CSV headers

    # Blocks loading and elaboration
    total_processed = 0
    for chunk in pd.read_csv(dataset_file, chunksize=chunksize):
        # Email cleaning
        chunk["cleaned_message"] = chunk["message"].apply(clean_email_text)

        # Saving chunks results
        chunk[["file", "cleaned_message"]].to_csv(output_file, mode="a", header=False, index=False)

        total_processed += len(chunk)
        print(f"Processed {total_processed} emails...")

    print(f"Processing completed. Cleaned emails saved to {output_file}")


if __name__ == "__main__":
    dataset_file = "datasets/enron/enron.csv"
    output_file = "datasets/enron/cleaned_enron.csv"

    process_and_save_emails(dataset_file, output_file)

