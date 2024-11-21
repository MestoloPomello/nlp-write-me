from sklearn.metrics import silhouette_score
from results_handler import full_output


stage_name = "Evaluation"


def evaluate_clustering(results):
    for section, result in results.items():
        X = result["vectorized_data"]
        labels = result["labels"]
        score = silhouette_score(X, labels)

        full_output(
            stage=stage_name,
            text=f"Silhouette Score: {score}",
            newline=False
        )
        full_output(
            stage=stage_name,
            text=f"Top terms for each cluster in {section}:",
            newline=False
        )
        for i, terms in enumerate(result["top_terms"]):
            full_output(
                stage=stage_name,
                text=f"Cluster {i}: {', '.join(terms)}",
                newline=False
            )
