from sklearn.metrics import silhouette_score

def evaluate_clustering(X, labels):
    score = silhouette_score(X, labels)
    
    with open("clustering_evaluation.txt", "w") as file:
        file.write(f"Silhouette Score: {score}\n")
    
    print(f"Silhouette Score: {score}")

