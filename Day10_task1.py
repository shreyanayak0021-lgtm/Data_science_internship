import pandas as pd

df = pd.read_csv("customer_orders.csv")

# Shape before cleaning
print("Shape before cleaning:", df.shape)

print("\nOriginal Data:\n", df)

# Missing values report
print("\nMissing values:\n", df.isna().sum())

# Fill missing numeric values with median
df['order_id']=df['order_id'].fillna(df['order_id'].median())
# Identify duplicate rows
print("\nDuplicate rows:\n", df[df.duplicated()])
print(df)

# Remove duplicates
df = df.drop_duplicates()
print(df)

# Shape after cleaning
print("\nShape after cleaning:", df.shape)

print("\nFinal Cleaned Data:\n", df)
