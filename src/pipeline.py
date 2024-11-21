import argparse
from results_handler import initialize
from stages.preprocessing import preprocess_data
from stages.clustering import cluster_sections
from stages.classification import classify_sections
from stages.evaluation import evaluate_clustering
from utils import printf


def main(dataset_file, num_emails, custom_random_state):
    # Initialization
    printf("[Initialization] Started")
    initialize(custom_random_state, num_emails)

    printf("-----------------------------------------------------")

    # Step 1: Preprocessing
    printf("[Preprocessing] Started")
    email_data = preprocess_data(dataset_file, num_emails)

    printf("-----------------------------------------------------")

    # Step 2: Clustering
    printf("[Clustering] Started")
    results = cluster_sections(email_data)

    printf("-----------------------------------------------------")

    # Step 3: Classification
    # printf("[Classification] Started")
    # results = classify_sections(vectorized_data, labels)

    # printf("-----------------------------------------------------")

    # Step 4: Evaluation
    printf("[Evaluation] Started")
    evaluate_clustering(results)

    printf("-----------------------------------------------------")

    printf("Pipeline completed successfully.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process email dataset.")
    parser.add_argument(
        "dataset_file",
        type=str,
        help="Path to the CSV dataset file"
    )
    parser.add_argument(
        "--num_emails",
        default=5,
        type=int,
        help="Number of emails to process"
    )
    parser.add_argument(
        "--random_state",
        default=-1,
        type=int,
        help="Custom random state"
    )

    '''
    parser.add_argument(
        "--random",
        action="store_true",
        help="Select emails randomly"
        )
    '''

    args = parser.parse_args()
    main(args.dataset_file, args.num_emails, args.random_state)
