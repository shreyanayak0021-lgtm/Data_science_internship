import pandas as pd
import numpy as np
data = {
    "values": [45, 50, 52, 47, 49, 51, 300]
}

df = pd.DataFrame(data)
mu = df["values"].mean()
sigma = df["values"].std()

print("Mean (μ):", mu)
print("Standard Deviation (σ):", sigma)

df["z_score"] = (df["values"] - mu) / sigma
outliers = df[np.abs(df["z_score"]) > 3]

print("\nDataset with Z-Scores:")
print(df)

print("\nStatistical Outliers (|Z| > 3):")
print(outliers)
