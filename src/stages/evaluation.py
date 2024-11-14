from sklearn.metrics import silhouette_score
from results_handler import full_output


def evaluate_clustering(X, labels):
    score = silhouette_score(X, labels)
    full_output(stage="Evaluation", text=f"Silhouette Score: {score}")
