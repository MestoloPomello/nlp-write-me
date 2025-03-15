import re
import pandas as pd

def extract_email_texts(file_path, output_file):
    # Extract ONLY the email bodies from an unstructured file and save them in a CSV.
    # The email bodies are separated by blocks that start with "From r ..." and end with "Status: ..."
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()

    # Split emails based on "From r ..." (first element is empty, ignore it)
    email_blocks = re.split(r"\nFrom r .*?\n", data)[1:]

    email_texts = []

    for email in email_blocks:
        # Remove headers (from start to "Status: ...")
        email_body = re.sub(r".*?\nStatus: .*\n", "", email, flags=re.DOTALL).strip()

        if email_body:  # To avoid appending empty emails
            email_texts.append(email_body)

    # Create a DataFrame with a progressive ID
    df = pd.DataFrame({"id": range(1, len(email_texts) + 1), "text": email_texts})
    df.to_csv(output_file, index=False)

    print(f"Dataset saved in {output_file} with {len(email_texts)} emails.")
    return df



if __name__ == "__main__":
    extract_email_texts("datasets/fraudulent/fraudulent_full.txt", output_file = "datasets/fraudulent/fraudulent_clean.csv")

