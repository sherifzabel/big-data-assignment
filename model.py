import pandas as pd
from sklearn.cluster import KMeans

# Input and output paths inside the Docker container
input_path = "/home/doc-bd-a1/res_dpre.csv"
output_path = "/home/doc-bd-a1/k.txt"

# Read the CSV
data = pd.read_csv(input_path)
print("Dataset loaded successfully for KMeans clustering.")

# Select only numeric columns for clustering
numeric_data = data[['Survived', 'Pclass', 'Age']]

# Apply KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(numeric_data)
data['Cluster'] = kmeans.labels_

# Save cluster information to a file
with open(output_path, 'w') as file:
    for i in range(3):
        # Get the number of records in each cluster
        cluster_label = i
        cluster_size = (data['Cluster'] == cluster_label).sum()
        file.write(f'Cluster({cluster_label}) has: {cluster_size} records\n')

print(f"Cluster information saved to: {output_path}")
