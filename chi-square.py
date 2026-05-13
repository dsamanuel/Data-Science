import numpy as np
from scipy.stats import chi2_contingency

# Input the contingency table counts
data = np.array([[71, 107, 114],
                 [15, 44, 16]])

# Run the Chi-Square Test of Independence
# correction=True applies Yates' correction automatically for 2x2 tables
stat, p, dof, expected = chi2_contingency(data)

# Output results
print(f"Chi-Square Statistic: {stat:.4f}")
print(f"P-value: {p}")
print(f"Degrees of Freedom: {dof}")
print("Expected Frequencies Table:")
print(expected)

# Interpret the findings
alpha = 0.05
if p < alpha:
    print("\nReject the null hypothesis: Significant association between variables.")
else:
    print("\nFail to reject the null hypothesis: No significant association found.")
