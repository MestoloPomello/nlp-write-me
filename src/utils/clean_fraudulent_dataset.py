import re
import pandas as pd

def extract_email_texts(file_path, output_file):
    """
    Estrae SOLO il corpo del testo delle email da un file non strutturato e lo salva in un CSV.
    Il testo delle email è separato da blocchi che iniziano con "From r ..." e finiscono con "Status: ...".
    """
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()

    # Dividere le email in base a "From r ..." (primo elemento è vuoto, lo ignoriamo)
    email_blocks = re.split(r"\nFrom r .*?\n", data)[1:]

    email_texts = []

    for email in email_blocks:
        # Rimuove gli header (dall'inizio fino a "Status: ...")
        email_body = re.sub(r".*?\nStatus: .*\n", "", email, flags=re.DOTALL).strip()

        if email_body:  # Evita di aggiungere email vuote
            email_texts.append(email_body)

    # Creare un DataFrame con un ID progressivo
    df = pd.DataFrame({"id": range(1, len(email_texts) + 1), "text": email_texts})

    # Salvare il dataset pulito in CSV
    df.to_csv(output_file, index=False)

    print(f"Dataset salvato in {output_file} con {len(email_texts)} email.")
    return df



if __name__ == "__main__":
    extract_email_texts("datasets/fraudulent/fraudulent_full.txt", output_file = "datasets/fraudulent/fraudulent_clean.csv")

