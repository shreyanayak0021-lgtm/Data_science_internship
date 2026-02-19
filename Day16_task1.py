import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

np.random.seed(0)

# Normal Data (Heights)
heights = np.random.normal(170, 10, 1000)

# Right Skewed Data (Income)
income = np.random.exponential(50000, 1000)

# Left Skewed Data (Easy Exam Scores)
scores = 100 - np.random.exponential(10, 1000)


def analyze(data, title):
    df = pd.DataFrame(data, columns=["Values"])
    
    mean = df["Values"].mean()
    median = df["Values"].median()
    
    print("\n", title)
    print("Mean =", round(mean, 2))
    print("Median =", round(median, 2))
    
    if mean > median:
        print("Right-Skewed")
    elif mean < median:
        print("Left-Skewed")
    else:
        print("Normal Distribution")
    
    # Histogram
    plt.figure()
    plt.hist(df["Values"], bins=30, density=True)
    
    # KDE line
    kde = gaussian_kde(df["Values"])
    x = np.linspace(min(df["Values"]), max(df["Values"]), 1000)
    plt.plot(x, kde(x))
    
    plt.title(title)
    plt.xlabel("Values")
    plt.ylabel("Density")
    plt.show()
# Run analysis
analyze(heights, "Human Heights (Normal)")
analyze(income, "Household Income (Right-Skewed)")
analyze(scores, "Easy Exam Scores (Left-Skewed)")
