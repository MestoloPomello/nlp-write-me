import sys
from stages.preprocessing import preprocess_data
from stages.clustering import cluster_sections
from stages.classification import classify_sections
from stages.evaluation import evaluate_clustering

def main(dataset_file, num_emails):
    # Step 1: Preprocessing
    print("Starting preprocessing...")
    email_data = preprocess_data(dataset_file, num_emails)
    
    # Step 2: Clustering
    print("Clustering sections...")
    labels, vectorized_data = cluster_sections(email_data)
    
    # Step 3: Classification
    print("Classifying sections...")
    classifications = classify_sections(vectorized_data, labels)
    
    # Step 4: Evaluation
    print("Evaluating clustering consistency...")
    evaluate_clustering(vectorized_data, labels)

    print("Pipeline completed successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pipeline.py <dataset_file> <num_emails>")
        sys.exit(1)
    
    dataset_file = sys.argv[1]
    num_emails = int(sys.argv[2])
    main(dataset_file, num_emails)

