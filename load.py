import sys
import pandas as pd
import subprocess

# Accept the dataset file path as a command-line argument
dataset_path = sys.argv[1]

# Read the dataset
try:
    data = pd.read_csv(dataset_path)
    print(f"Dataset loaded successfully from: {dataset_path}")
except FileNotFoundError:
    print(f"Error: The dataset file at {dataset_path} was not found.")
    sys.exit(1)

# Save the updated dataset within the container
output_path = "/home/doc-bd-a1/updated_data.csv"
data.to_csv(output_path, index=False)
print(f"Dataset saved to: {output_path}")

# Trigger the next script in the pipeline (dpre.py)
try:
    subprocess.run(["python3", "/home/doc-bd-a1/dpre.py"], check=True)
    print("dpre.py executed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error while executing dpre.py: {e}")
    sys.exit(1)
