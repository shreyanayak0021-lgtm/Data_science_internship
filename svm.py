import numpy as np
import matplotlib.pyplot as plt

# Original 1D data
x = np.array([-2, -1, 0, 1, 2])

# Map to 2D: (x, x^2)
x2 = x**2

mapped_points = list(zip(x, x2))
print("Mapped points:", mapped_points)

# Plot the mapped points
plt.scatter(x, x2)

# Highlight the special point (0,0)
plt.scatter(0, 0, marker='x', s=200)

# Decision boundary y = 0.5
plt.axhline(1.0)

# Labels
plt.xlabel("x")
plt.ylabel("x^2")
plt.title("1D to 2D Mapping Example")

plt.show()