import pandas as pd

# Load the dataset
file_path = "Data/StudentsPerformance.csv"  # Update with the correct path if needed
df = pd.read_csv(file_path)

# Check for null values
print("Null values in each column:")
print(df.isnull().sum())

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
#file_path = "/StudentsPerformance.csv"  # Update with the correct path
df = pd.read_csv(file_path)

# Set plot style
sns.set_style("whitegrid")

# Define numerical columns
numerical_cols = ["math score", "reading score", "writing score"]

# Create boxplots for each numerical column
plt.figure(figsize=(12, 5))
for i, col in enumerate(numerical_cols, 1):
    plt.subplot(1, 3, i)
    sns.stripplot(y=df[col], jitter=True, color="blue", alpha=0.5)
    plt.title(f"Strip Plot of {col}")

plt.tight_layout()
plt.show()
