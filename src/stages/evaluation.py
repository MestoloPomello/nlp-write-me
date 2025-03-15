import numpy as np
from sklearn.metrics import silhouette_score
from sklearn.metrics import davies_bouldin_score
from sklearn.metrics import calinski_harabasz_score
from sklearn.metrics import pairwise_distances_argmin_min
from results_handler import full_output
from collections import Counter


stage_name = "Evaluation"

# TUTTO DA RIVEDERE

def evaluate_clustering(results):
    for section, result in results.items():
        X = result["vectorized_data"]
        labels = result["labels"]

        # Silhouette Score
        score = silhouette_score(X, labels)
        full_output(
            stage=stage_name,
            text=f"{section} - Silhouette Score: {score}",
            newline=True
        )

        # Davies-Bouldin Index
        # dbi_score = davies_bouldin_score(X.toarray(), labels)
        # full_output(
        #     stage=stage_name,
        #     text=f"{section} - Davies-Bouldin Index: {dbi_score}",
        #     newline=True
        # )

        # Calinski-Harabasz Score
        chi_score = calinski_harabasz_score(X, labels)
        full_output(
            stage=stage_name,
            text=f"{section} - Calinski-Harabasz Index: {chi_score}",
            newline=True
        )

        # Cluster Size Consistency
        cluster_sizes = Counter(labels)
        std_dev = np.std(list(cluster_sizes.values()))
        full_output(
            stage=stage_name,
            text=f"{section} - Cluster Size Standard Deviation: {std_dev}",
            newline=True
        )

        # Top terms per cluster
        centroids = result["kmeans"].cluster_centers_
        avg_distances = [
            np.mean(pairwise_distances_argmin_min(
                X[labels == i],
                centroids[i]
            )[1])
            for i in range(len(centroids))
        ]
        for i, dist in enumerate(avg_distances):
            full_output(
                stage=stage_name,
                text=f"{section} - Average Distance to Centroid for Cluster {i}: {dist}",
                newline=True
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
