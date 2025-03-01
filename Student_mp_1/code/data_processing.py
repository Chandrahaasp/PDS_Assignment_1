import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "Data/StudentsPerformance.csv"  # Update with the correct path
df = pd.read_csv(file_path)

sns.set_style("whitegrid")

# 1. Math Score vs. Gender
plt.figure(figsize=(8, 5))
sns.boxplot(x="gender", y="math score", data=df, palette="Set2")
plt.title("Math Score Distribution by Gender")
plt.xlabel("Gender")
plt.ylabel("Math Score")
plt.show()

# 2. Race/Ethnicity vs. Parental Level of Education
plt.figure(figsize=(10, 5))
sns.countplot(x="race/ethnicity", hue="parental level of education", data=df, palette="coolwarm")
plt.title("Parental Education Level Across Race/Ethnicity Groups")
plt.xlabel("Race/Ethnicity")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.legend(title="Parental Education Level")
plt.show()

# 3. Test Preparation Course vs. Reading Score
plt.figure(figsize=(8, 5))
sns.boxplot(x="test preparation course", y="reading score", data=df, palette="Set1")
plt.title("Reading Scores Based on Test Preparation")
plt.xlabel("Test Preparation Course")
plt.ylabel("Reading Score")
plt.show()

# 4. Writing Score vs. Gender
plt.figure(figsize=(8, 5))
sns.boxplot(x="gender", y="writing score", data=df, palette="muted")
plt.title("Writing Score Distribution by Gender")
plt.xlabel("Gender")
plt.ylabel("Writing Score")
plt.show()

# 5. Gender vs. Lunch Plan
plt.figure(figsize=(8, 5))
sns.countplot(x="gender", hue="lunch", data=df, palette="pastel")
plt.title("Lunch Plan Distribution by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.legend(title="Lunch Plan")
plt.show()
