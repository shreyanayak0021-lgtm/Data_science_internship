import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
population = np.random.exponential(scale=2, size=10000)

sample_means = []

for i in range(1000):
    sample = np.random.choice(population, size=30)
    mean_of_sample = np.mean(sample)
    sample_means.append(mean_of_sample)

plt.figure()
plt.hist(sample_means, bins=30)
plt.title("Histogram of 1000 Sample Means (n = 30)")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.show()
