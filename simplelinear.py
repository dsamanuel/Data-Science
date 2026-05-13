import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Prepare dummy data
X = np.array([[1], [2], [3], [4], [5]])  # Features (must be 2D array)
y = np.array([2, 3.9, 6.1, 8.0, 10.2])   # Target variable

# 2. Initialize and train the model
model = LinearRegression()
model.fit(X, y)

# 3. Make a new prediction
new_input = np.array([[6]])
prediction = model.predict(new_input)

# 4. Extract model metrics
print(f"Intercept (Beta 0): {model.intercept_}")
print(f"Coefficient (Beta 1): {model.coef_[0]}")
print(f"Prediction for x=6: {prediction[0]}")
