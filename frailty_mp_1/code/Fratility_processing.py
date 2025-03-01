import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/Fratility_raw.csv") 

# Convert weight from pounds to kilograms and height from inches to meters
df['Weight_kg'] = df['Weight'] * 0.453592
df['Height_m'] = df['Height'] * 0.0254

# Calculate BMI (Body Mass Index)
df['BMI'] = df['Weight_kg'] / (df['Height_m'] ** 2)

# Set up the figure
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Plot 1: Grip Strength vs. Age
axes[0].scatter(df[df['Frailty'] == 'N']['Grip strength'], 
                df[df['Frailty'] == 'N']['Age'], 
                color='blue', 
                label='Frailty = N', 
                s=100, edgecolors='black')

axes[0].scatter(df[df['Frailty'] == 'Y']['Grip strength'], 
                df[df['Frailty'] == 'Y']['Age'], 
                color='red', 
                label='Frailty = Y', 
                s=100, edgecolors='black')

axes[0].set_title('Grip Strength vs Age (by Frailty Status)', fontsize=14)
axes[0].set_xlabel('Grip Strength (kg)', fontsize=12)
axes[0].set_ylabel('Age (years)', fontsize=12)
axes[0].legend()

# Plot 2: Grip Strength vs. BMI
axes[1].scatter(df[df['Frailty'] == 'N']['Grip strength'], 
                df[df['Frailty'] == 'N']['BMI'], 
                color='blue', 
                label='Frailty = N', 
                s=100, edgecolors='black')

axes[1].scatter(df[df['Frailty'] == 'Y']['Grip strength'], 
                df[df['Frailty'] == 'Y']['BMI'], 
                color='red', 
                label='Frailty = Y', 
                s=100, edgecolors='black')

axes[1].set_title('Grip Strength vs BMI (by Frailty Status)', fontsize=14)
axes[1].set_xlabel('Grip Strength (kg)', fontsize=12)
axes[1].set_ylabel('BMI (kg/m²)', fontsize=12)
axes[1].legend()

# Adjust layout and show the plots
plt.tight_layout()
plt.show()
