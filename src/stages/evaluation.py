import os
from sklearn.metrics import silhouette_score
from datetime import datetime

def evaluate_clustering(X, labels):
    score = silhouette_score(X, labels)

    # Build file path
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    evaluation_dir = os.path.join(project_root, "evaluations")
    os.makedirs(evaluation_dir, exist_ok=True)

    now = datetime.now()
    file_name = f"clustering_evaluation_{now.month}{now.day}_{now.hour:02d}{now.minute:02d}{now.second:02d}.txt"
    path = os.path.join(evaluation_dir, file_name)

    with open(path, "w") as file:
        file.write(f"Silhouette Score: {score}\n")
    
    print(f"Silhouette Score: {score}")
    print(f"Results saved in {path}")

