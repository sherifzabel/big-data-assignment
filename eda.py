# import pandas as pd

# # Read the CSV
# data = pd.read_csv(r"C:\Users\sheri\OneDrive\Desktop\bd-a1\res_dpre.csv")


# # Insight 1: Age
# age_mean = data['Age'].mean()
# age_median = data['Age'].median()
# age_std = data['Age'].std()
# insight_1 = f"Insight 1: Age Distribution\nMean Age: {age_mean}\nMedian Age: {age_median}\nStandard Deviation of Age: {age_std}"

# # Insight 2: Survival Rate
# survival_rate = data['Survived'].mean() * 100
# insight_2 = f"Insight 2: Survival Rate\nSurvival Rate: {survival_rate:.2f}%"

# # Insight 3: Age Category Distribution
# age_category_counts = data['Age_category'].value_counts()
# insight_3 = f"Insight 3: Age Category Distribution\n{age_category_counts}"

# # Save insights to text files
# with open('eda-in-1.txt', 'w') as file:
#     file.write(insight_1)

# with open('eda-in-2.txt', 'w') as file:
#     file.write(insight_2)

# with open('eda-in-3.txt', 'w') as file:
#     file.write(insight_3)


import pandas as pd

# Input and output paths inside the Docker container
input_path = "/home/doc-bd-a1/res_dpre.csv"
output_dir = "/home/doc-bd-a1/"

# Read the processed CSV file
data = pd.read_csv(input_path)
print("Data loaded successfully for EDA.")

# Insight 1: Age Distribution
if 'Age' in data.columns:
    age_mean = data['Age'].mean()
    age_median = data['Age'].median()
    age_std = data['Age'].std()
    insight_1 = (
        f"Insight 1: Age Distribution\n"
        f"Mean Age: {age_mean:.2f}\n"
        f"Median Age: {age_median:.2f}\n"
        f"Standard Deviation of Age: {age_std:.2f}"
    )
else:
    insight_1 = "Insight 1: Age Distribution\nColumn 'Age' is missing."

# Insight 2: Survival Rate
if 'Survived' in data.columns:
    survival_rate = data['Survived'].mean() * 100
    insight_2 = f"Insight 2: Survival Rate\nSurvival Rate: {survival_rate:.2f}%"
else:
    insight_2 = "Insight 2: Survival Rate\nColumn 'Survived' is missing."

# Insight 3: Family Size Distribution
if 'SibSp' in data.columns and 'Parch' in data.columns:
    data['FamilySize'] = data['SibSp'] + data['Parch']
    family_size_counts = data['FamilySize'].value_counts()
    insight_3 = (
        f"Insight 3: Family Size Distribution\n"
        f"{family_size_counts.to_string()}"
    )
else:
    insight_3 = "Insight 3: Family Size Distribution\nColumns 'SibSp' and 'Parch' are missing."

# Save insights to text files
with open(f"{output_dir}eda-in-1.txt", 'w') as file:
    file.write(insight_1)

with open(f"{output_dir}eda-in-2.txt", 'w') as file:
    file.write(insight_2)

with open(f"{output_dir}eda-in-3.txt", 'w') as file:
    file.write(insight_3)

# Save the modified data back to a CSV (if needed)
data.to_csv(f"{output_dir}res_eda.csv", index=False)

print("EDA processing completed successfully. Insights saved.")
