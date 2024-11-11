import sys
import argparse
from stages.preprocessing import preprocess_data
from stages.clustering import cluster_sections
from stages.classification import classify_sections
from stages.evaluation import evaluate_clustering

def main(dataset_file, num_emails, random_selection):
    # Step 1: Preprocessing
    print("Starting preprocessing...")
    email_data = preprocess_data(dataset_file, num_emails, random_selection)
    
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
    parser = argparse.ArgumentParser(description="Process email dataset.")
    parser.add_argument("dataset_file", type=str, help="Path to the CSV dataset file")
    parser.add_argument("num_emails", type=int, help="Number of emails to process")
    parser.add_argument("--random", action="store_true", help="Select emails randomly")

    args = parser.parse_args()
    main(args.dataset_file, args.num_emails, args.random)

