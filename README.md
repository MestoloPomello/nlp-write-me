“Quanto è efficace un sistema di estrazione di strutture di email basato su tecniche di NLP non supervisionate nel distinguere correttamente tra elementi strutturali e non strutturali?”

"How effective is an email structure extraction system based on unsupervised NLP techniques about correctly distinguishing between structural and non-structural elements?"

---

Move to the `src` directory before running the entry point.  
Execution: `python .\pipeline.py <dataset_file> --num_emails <num_emails> [--random_state <number>]`
- `dataset_file`: path to the CSV dataset file (or a hardcoded alias)
- `--num_emails`: how many emails to process, defaults to 5
- `--random_state`: random state for the steps that use it, defaults to a random value. Set this if you need to repeat a test on a previous group of emails

---

Example: `python .\pipeline.py fraud --num_emails 15000`
