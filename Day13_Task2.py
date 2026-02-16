import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------
# Sample Dataset
# ---------------------------------------
df = pd.DataFrame({
    'Price': [250000, 450000, 320000, 600000, 280000,
              500000, 350000, 400000, 550000, 300000],
    'SquareFootage': [1200, 2000, 1500, 3000, 1100,
                      2200, 1600, 1800, 2500, 1300],
    'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Chicago',
             'Los Angeles', 'New York', 'Chicago', 'Los Angeles', 'New York']
})

# ---------------------------------------
# 1️⃣ Scatter Plot: SquareFootage vs Price
# ---------------------------------------
sns.scatterplot(x='SquareFootage', y='Price', data=df, color='skyblue', s=100)
plt.title("Scatter Plot: Price vs SquareFootage")
plt.xlabel("SquareFootage")
plt.ylabel("Price")
plt.show()

# ---------------------------------------
# 2️⃣ Boxplot: City vs Price
# ---------------------------------------
sns.boxplot(x='City', y='Price', data=df)
plt.title("Boxplot: Price by City")
plt.xlabel("City")
plt.ylabel("Price")
plt.show()

# ---------------------------------------
# 3️⃣ Observation
# ---------------------------------------
print("Observation: As SquareFootage increases, Price seems to increase.")
