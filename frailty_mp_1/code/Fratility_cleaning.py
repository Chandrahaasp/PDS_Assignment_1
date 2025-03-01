import pandas as pd

# Load data
df = pd.read_csv("data/Fratility_raw.csv")  

# Display first 5 rows
print(df.head())


null_values = df.isnull().sum()

# Print null values for each column
print("Null values in each column:")
print(null_values)


# Encoding the 'Frailty' column (Y/N -> 1/0)
df['Frailty'] = df['Frailty'].map({'Y': 1, 'N': 0})

# Check the first few rows after encoding
print(df.head())


print("\nSummary Statistics:")
print(df.describe())
