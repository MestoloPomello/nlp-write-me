import argparse
from results_handler import initialize, output_processed_emails
# from stages.preprocessing_enron import preprocess_data, extract_bodies
from stages.preprocessing_nigeria import preprocess_data
# from stages.OLD_topic_modeling import topic_modeling, assign_topics
from stages.clustering import cluster_sections
from stages.classification import classify_email_dataset
from stages.evaluation import evaluate_clustering
from utils import printf
from stages.topic_modeling import run_topic_modeling


def main(dataset_file, num_emails, custom_random_state):
    # Initialization
    printf("[Initialization] Started")
    initialize(custom_random_state, num_emails)

    printf("-----------------------------------------------------")

    # Step 1: Preprocessing
    printf("[Preprocessing] Started")
    email_data = preprocess_data(dataset_file, num_emails)

    # print("email_data\n", email_data)
    # email_bodies = extract_bodies(email_data)

    printf("-----------------------------------------------------")

    # Step 2: Classification
    printf("[Classification] Structural Parts Classification Started")
    # results = classify_sections(vectorized_data, labels)
    df_after_classification = classify_email_dataset(email_data["body"])    # Risultato stampato giusto

    printf("-----------------------------------------------------")

    # Step 3: Topic Modeling
    df_after_tm = run_topic_modeling(df_after_classification)
    
    output_processed_emails(df_after_tm)

    # printf("[Topic Modeling] Started")
    # topics, lda, X = topic_modeling(email_bodies, n_topics=5)

    # printf("[Topic Modeling] Assigning topics to emails")
    # assigned_topics = assign_topics(lda, X)

    # printf("\nTop topics identified:")
    # for idx, topic in enumerate(topics):
    #     printf(f"Topic {idx}: {', '.join(topic)}")

    # printf("\nEmail-to-Topic Mapping:")
    # for i, topic in enumerate(assigned_topics):
    #     printf(f"Email {i+1}: Topic {topic}")

    # Step 2: Clustering
    # printf("[Clustering] Started")
    # results = cluster_sections(email_data)

    # printf("-----------------------------------------------------")

    return

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
