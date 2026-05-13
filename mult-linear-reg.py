import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Generate synthetic data (e.g., Housing Market: Size, Bedrooms, Age -> Price)
np.random.seed(42)
n_samples = 100

data = {
    'Size_SQFT': np.random.randint(1000, 3500, n_samples),
    'Bedrooms': np.random.randint(1, 5, n_samples),
    'Age_Years': np.random.randint(0, 50, n_samples)
}
df = pd.DataFrame(data)

# Target formula with random noise injected
df['Price_USD'] = (df['Size_SQFT'] * 150) + (df['Bedrooms'] * 10000) - (df['Age_Years'] * 500) + np.random.normal(0, 5000, n_samples)

# 2. Separate Features (X) and Target (y)
X = df[['Size_SQFT', 'Bedrooms', 'Age_Years']]
y = df['Price_USD']

# 3. Split data into Training (80%) and Testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Initialize and fit the Multiple Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Predict on the test set
y_pred = model.predict(X_test)

# 6. Evaluate model quality
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Intercept (Beta 0): {model.intercept_:.2f}")
print(f"Coefficients (Beta 1, 2, 3): {model.coef_}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared Score (R2): {r2:.4f}")
