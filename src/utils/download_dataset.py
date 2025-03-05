import kagglehub

# Download latest version
path = kagglehub.dataset_download("amank56/enron-clean-dataset")

print("Path to dataset files:", path)