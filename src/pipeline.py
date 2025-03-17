import argparse
from results_handler import initialize, output_processed_emails
from stages.preprocessing import preprocess_data
from stages.classification import classify_email_dataset
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

    printf("-----------------------------------------------------")

    # Step 2: Classification
    printf("[Structural Classification] Started")
    df_after_classification = classify_email_dataset(email_data["body"])

    printf("-----------------------------------------------------")

    # Step 3: Topic Modeling
    printf("[Topic Modeling] Started")
    df_after_tm = run_topic_modeling(df_after_classification)
    output_processed_emails(df_after_tm)

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
