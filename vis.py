import pandas as pd
import matplotlib.pyplot as plt

# Input path inside the Docker container
input_path = "/home/doc-bd-a1/res_dpre.csv"
output_path = "/home/doc-bd-a1/vis.png"

# Read the CSV
data = pd.read_csv(input_path)
print("Dataset loaded successfully for visualization.")

# Create a visualization based on the 'Pclass' column
pclass_counts = data['Pclass'].value_counts().sort_index()

# Create a bar chart
plt.bar(pclass_counts.index, pclass_counts.values)

# Set labels and title
plt.xlabel('Pclass')
plt.ylabel('Frequency')  # The y-axis represents frequency of Pclass, not Age
plt.title('Survival by Pclass')

# Save the visualization as a PNG file inside the container
plt.savefig(output_path)
print(f"Visualization saved to: {output_path}")
