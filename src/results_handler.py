import os
import random
from datetime import datetime
from utils import printf


results_file_path = ""
processed_emails_file_path = ""
random_state = -1


def initialize(custom_random_state, num_emails):
    # Build file path
    project_root = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
    evaluations_dir = os.path.join(project_root, "evaluations")
    os.makedirs(evaluations_dir, exist_ok=True)

    now = datetime.now()
    folder_name = f"clustering_evaluation_{now.month}{now.day}_{now.hour:02d}{now.minute:02d}{now.second:02d}"
    os.makedirs(os.path.join(evaluations_dir, folder_name), exist_ok=True)

    # Setup the results file
    global results_file_path
    results_file_path = os.path.join(evaluations_dir, folder_name, "results.txt")

    # Setup the processed emails file
    global processed_emails_file_path
    processed_emails_file_path = os.path.join(evaluations_dir, folder_name, "processed_emails.csv")
    with open(processed_emails_file_path, "w") as file:
        file.write("sep=,\ngreeting,body,closing\n")

    if custom_random_state == -1:
        global random_state
        random_state = random.randint(1, 10000)

    full_output(
        stage="Initialization",
        text=f"Number of emails: {num_emails} | Random State: {random_state}",
        newline=False
    )

    printf(f"results_file_path", results_file_path)
    printf(f"[Initialization] Data will be saved to: /evaluations/{folder_name}/")


def append_to_results(text, newline=False):
    with open(results_file_path, "a") as file:
        str = f"{text}\n"
        if newline is True:
            str = "\n" + str
        file.write(str)
        # file.write("------------------------------------------")
        # file.write("\n\n")


def append_to_processed_emails(single_processed_email):
    body_str = " ".join(single_processed_email["body"]).strip()
    with open(processed_emails_file_path, "a", encoding="utf-8") as file:
        str = f"{single_processed_email["greeting"]},{body_str},{single_processed_email["closing"]}\n"
        file.write(str)


def full_output(stage, text, newline=False):
    full_string = f"[{stage}] {text}"
    printf(full_string)
    append_to_results(full_string, newline)


def get_random_state():
    return random_state
