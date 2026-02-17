import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Step 1: Create Sample Data
data = pd.DataFrame({
    'Age': [22, 25, 30, 35, 40, 45, 50],
    'Salary': [25000, 30000, 50000, 70000, 90000, 120000, 150000]
})

print("Original Data:\n", data)

# Step 2: Standardization (Mean = 0, Std = 1)
standard_scaler = StandardScaler()
standardized_data = standard_scaler.fit_transform(data)
standardized_df = pd.DataFrame(standardized_data, columns=data.columns)

print("\nStandardized Data:\n", standardized_df)

# Step 3: Normalization (0 to 1)
minmax_scaler = MinMaxScaler()
normalized_data = minmax_scaler.fit_transform(data)
normalized_df = pd.DataFrame(normalized_data, columns=data.columns)

print("\nNormalized Data:\n", normalized_df)

# Step 4: Plot Histograms (Salary Before and After Scaling)

plt.figure(figsize=(15,4))

# Original
plt.subplot(1,3,1)
plt.hist(data['Salary'], bins=5)
plt.title("Original Salary")
plt.xlabel("Salary")

# Standardized
plt.subplot(1,3,2)
plt.hist(standardized_df['Salary'], bins=5)
plt.title("Standardized Salary")
plt.xlabel("Standardized")

# Normalized
plt.subplot(1,3,3)
plt.hist(normalized_df['Salary'], bins=5)
plt.title("Normalized Salary")
plt.xlabel("Normalized (0-1)")

plt.tight_layout()
plt.show()
