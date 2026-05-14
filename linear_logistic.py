import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

# 1. Dummy Data: Hours studied vs. Exam Outcomes
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])

# Linear target: Actual exam score out of 100
y_linear = np.array([45, 50, 58, 65, 72, 80, 88, 95])

# Logistic target: Pass (1) or Fail (0)
y_logistic = np.array([0, 0, 0, 0, 1, 1, 1, 1])

# 2. Fit Linear Regression Model
lin_model = LinearRegression()
lin_model.fit(X, y_linear)

# 3. Fit Logistic Regression Model
log_model = LogisticRegression()
log_model.fit(X, y_logistic)

# 4. Generate Predictions for a student who studied 4.5 hours
new_student = np.array([[4.5]])

lin_pred = lin_model.predict(new_student)
log_pred_class = log_model.predict(new_student)
log_pred_proba = log_model.predict_proba(new_student)

# 5. Output Comparison
print(f"Linear Regression Prediction (Score): {lin_pred[0]:.2f}")
print(f"Logistic Regression Predicted Class (0=Fail, 1=Pass): {log_pred_class[0]}")
print(f"Logistic Regression Probability Matrix [P(0), P(1)]: {log_pred_proba[0]}")
