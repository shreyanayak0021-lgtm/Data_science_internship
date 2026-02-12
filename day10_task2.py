import pandas as pd

df = pd.DataFrame({
    "Price": ["$100", "$200", "$100.5"],
    "Date": ["01-02-2026", "05-02-2026", "10-02-2026"]
})

print(df.dtypes)
df['Price']=df['Price'].str.replace("$","",regex=False)
df['Price']=df['Price'].astype(float)
df['Date'] = pd.to_datetime(df["Date"], format="%d-%m-%Y")

print("After:\n",df.dtypes)

print("final:\n",df)