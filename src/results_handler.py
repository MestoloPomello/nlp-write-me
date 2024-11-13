import os
import random
from datetime import datetime

results_file_path = ""
random_state = -1

def initialize(custom_random_state):
    # Build file path
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    evaluation_dir = os.path.join(project_root, "evaluations")
    os.makedirs(evaluation_dir, exist_ok=True)

    now = datetime.now()
    file_name = f"clustering_evaluation_{now.month}{now.day}_{now.hour:02d}{now.minute:02d}{now.second:02d}.txt"

    global results_file_path
    results_file_path = os.path.join(evaluation_dir, file_name)

    if custom_random_state == -1:
        global random_state
        random_state = random.randint(1, 10000)

    append_to_results(f"Random State: {random_state}")

    print(f"[Initialization] Data will be saved to: {results_file_path}")

def append_to_results(text):
    with open(results_file_path, "a") as file:
        file.write(f"{text}\n\n")
        file.write("------------------------------------------")
        file.write("\n\n")

def get_random_state():
    return random_state
