import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

# Step 1: Create Non-Linear Data (y = x^2 relationship)
np.random.seed(42)
X = np.linspace(-5, 5, 100).reshape(-1, 1)
y = X**2 + np.random.normal(0, 3, 100).reshape(-1, 1)

# Step 2: Train Linear Regression on Original Feature
linear_model = LinearRegression()
linear_model.fit(X, y)
y_pred_linear = linear_model.predict(X)
r2_linear = r2_score(y, y_pred_linear)

# Step 3: Create Polynomial Features (degree=2)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Step 4: Train Linear Regression on Polynomial Features
poly_model = LinearRegression()
poly_model.fit(X_poly, y)
y_pred_poly = poly_model.predict(X_poly)
r2_poly = r2_score(y, y_pred_poly)

# Step 5: Print R2 Scores
print("R2 Score (Simple Linear Regression):", r2_linear)
print("R2 Score (Polynomial Regression degree=2):", r2_poly)

# Step 6: Plot Results
plt.scatter(X, y, label="Actual Data")
plt.plot(X, y_pred_linear, color='red', label="Linear Fit")
plt.plot(X, y_pred_poly, color='green', label="Polynomial Fit (degree=2)")
plt.legend()
plt.title("Linear vs Polynomial Regression")
plt.show()
