
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis

sns.set(style="whitegrid")

# -----------------------------
# Step 1 — Create Sample Dataset
# -----------------------------
data = {
    "Price": [250000, 300000, 150000, 400000, 500000, 320000, 450000, 200000, 270000, 380000,
              600000, 700000, 150000, 350000, 330000],
    "City": ["New York", "Los Angeles", "Chicago", "New York", "Chicago",
             "Los Angeles", "New York", "Chicago", "Los Angeles", "New York",
             "Chicago", "Los Angeles", "Chicago", "New York", "Los Angeles"]
}

df = pd.DataFrame(data)
print("Sample dataset:\n", df)

# -----------------------------
# Step 2 — Numerical Column: Price
# -----------------------------
num_col = 'Price'

# Histogram with KDE
plt.figure(figsize=(8,5))
sns.histplot(df[num_col], kde=True, bins=10, color='skyblue')
plt.title(f"Distribution of {num_col}")
plt.xlabel(num_col)
plt.ylabel("Frequency")
plt.show()

# Skewness & Kurtosis
num_skew = skew(df[num_col])
num_kurt = kurtosis(df[num_col])
print(f"Skewness of {num_col}: {num_skew:.2f}")
print(f"Kurtosis of {num_col}: {num_kurt:.2f}")

# -----------------------------
# Step 3 — Categorical Column: City
# -----------------------------
cat_col = 'City'

plt.figure(figsize=(8,5))
sns.countplot(data=df, x=cat_col, order=df[cat_col].value_counts().index, palette="Set2")
plt.title(f"Count Plot of {cat_col}")
plt.xlabel(cat_col)
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Print frequency counts
print(f"\nFrequency counts of {cat_col}:\n", df[cat_col].value_counts())
