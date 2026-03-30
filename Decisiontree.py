from sklearn.tree import DecisionTreeClassifier

# Features: [Study Hours]
X = [[1], [2], [3], [4], [5]]

# Target: 0 = Fail, 1 = Pass
y = [0, 0, 0, 1, 1]

# Create model
model = DecisionTreeClassifier()

# Train model
model.fit(X, y)

# Predict for a new student who studied 4 hours
prediction = model.predict([[4]])

print("Prediction:", prediction)