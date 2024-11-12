import os
from sklearn.metrics import silhouette_score
from datetime import datetime
from results_handler import append_to_results 

def evaluate_clustering(X, labels):
    score = silhouette_score(X, labels)

    append_to_results(f"Silhouette Score: {score}")
    
    print(f"Silhouette Score: {score}")

