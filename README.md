“Quanto è efficace un sistema basato su tecniche di NLP non supervisionate nel distinguere correttamente elementi strutturali e contestualizzare elementi non strutturali?”

"How effective is a system based on unsupervised NLP techniques about correctly distinguishing structural elements and contextualizing non-structural elements?"

---

Move to the `src` directory before running the entry point.  
Execution: `python .\pipeline.py <dataset_file> --num_emails <num_emails> [--random_state <number>]`
- `dataset_file`: path to the CSV dataset file (or a hardcoded alias, such as "fraud")
- `--num_emails`: how many emails to process, defaults to 5. Use -1 for the whole dataset (suggested for the fraud one)
- `--random_state`: random state for the steps that use it, defaults to a random value. Set this if you need to repeat a test on a previous group of emails

---

Example: `python ./pipeline.py fraud --num_emails 15000`
