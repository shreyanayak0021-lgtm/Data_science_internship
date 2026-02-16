import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
data = {
    "SquareFootage": [800,1000,1200,1500,1800,2000,2200,2500,3000,3500],
    "Price": [40000,50000,60000,75000,90000,110000,130000,160000,200000,500000],  # 500000 is an outlier
    "Bedrooms": [1,2,2,3,3,3,4,4,5,5],
    "Bathrooms": [1,1,2,2,2,3,3,3,4,4]
}
df = pd.DataFrame(data)
print("\nCorrelation Matrix:\n")
corr_matrix = df.corr()
print(corr_matrix)
plt.figure()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
print("\nHighly Correlated Features (>|0.8|):\n")
for i in range(len(corr_matrix.columns)):
    for j in range(i):
        if abs(corr_matrix.iloc[i, j]) > 0.8:
            col1 = corr_matrix.columns[i]
            col2 = corr_matrix.columns[j]
            corr_value = corr_matrix.iloc[i, j]
            print(f"{col1} and {col2} --> Correlation: {corr_value:.2f}")
plt.figure()
sns.boxplot(x=df["Price"])
plt.title("Price Outliers (Boxplot)")
plt.show()
Q1 = df["Price"].quantile(0.25)
Q3 = df["Price"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df["Price"] < lower_bound) | (df["Price"] > upper_bound)]
print("\nOutliers Detected Using IQR Method:\n")
print(outliers)