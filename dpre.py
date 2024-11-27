import pandas as pd
import numpy as np
import os
import subprocess

# Path to the dataset inside the Docker container
input_path = "/home/doc-bd-a1/tit_dataset.csv"
output_path = "/home/doc-bd-a1/res_dpre.csv"

# Read the CSV
data = pd.read_csv(input_path)
print("Data loaded successfully.")

# Check for missing values
missing_values = data.isnull().sum()
print("Missing values per column:\n", missing_values)

# Data structure and summary statistics
print(data.info())
print(data.describe())

# Data Cleaning: Fill missing values in 'Age' column with the mean
if 'Age' in data.columns:
    data['Age'] = data['Age'].fillna(data['Age'].mean())

# Data Transformation: Normalize 'Age' column
if 'Age' in data.columns:
    data['normalized_Age'] = (data['Age'] - data['Age'].min()) / (data['Age'].max() - data['Age'].min())

# Data Reduction: Select specific columns
# Replace 'Survived' and 'Pclass' with actual column names from your dataset
selected_columns = ['Survived', 'Pclass', 'normalized_Age', 'Age']
data = data[selected_columns]

# Data Discretization: Categorize 'Age' into bins
if 'Age' in data.columns:
    data['Age_category'] = pd.cut(data['Age'], bins=3, labels=["Low", "Medium", "High"])

# Save the processed data
data.to_csv(output_path, index=False)
print(f"Processed data saved to {output_path}")

# Trigger subsequent scripts
subprocess.run(["python3", "/home/doc-bd-a1/eda.py"])
subprocess.run(["python3", "/home/doc-bd-a1/model.py"])
subprocess.run(["python3", "/home/doc-bd-a1/vis.py"])
