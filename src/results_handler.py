import os
import random
from datetime import datetime
from utils import printf


results_file_path = ""
random_state = -1


def initialize(custom_random_state, num_emails):
    # Build file path
    project_root = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
    evaluation_dir = os.path.join(project_root, "evaluations")
    os.makedirs(evaluation_dir, exist_ok=True)

    now = datetime.now()
    file_name = "".join(
        [
            f"clustering_evaluation_{now.month}{now.day}_",
            f"{now.hour:02d}{now.minute:02d}{now.second:02d}.txt"
        ]
    )

    global results_file_path
    results_file_path = os.path.join(evaluation_dir, file_name)

    if custom_random_state == -1:
        global random_state
        random_state = random.randint(1, 10000)

    full_output(
        stage="Initialization",
        text=f"Number of emails: {num_emails} | Random State: {random_state}",
        newline=True
    )

    printf(f"[Initialization] Data will be saved to: /evaluations/{results_file_path.split("/evaluations/", 1)[1]}")


def append_to_results(text, newline=False):
    with open(results_file_path, "a") as file:
        str = f"{text}\n"
        if newline is True:
            str = str + "\n"
        file.write(str)
        # file.write("------------------------------------------")
        # file.write("\n\n")


def full_output(stage, text, newline=False):
    full_string = f"[{stage}] {text}"
    printf(full_string)
    append_to_results(full_string, newline)


def get_random_state():
    return random_state
