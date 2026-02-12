import pandas as pd

df = pd.DataFrame({
    "Location": [" New York", "new york", "NEW YORK "]
})

print("Before cleaning:\n", df)

# Remove leading/trailing spaces
df["Location"] = df["Location"].str.strip()

# Standardize casing (choose one)
df["Location"] = df["Location"].str.lower()



print("\nAfter cleaning:\n", df)
# Verify unique values
print("\nUnique values:\n", df["Location"].unique())
