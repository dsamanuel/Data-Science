import numpy as np
from scipy.stats import ttest_ind

# Sample continuous data for two independent groups
group_a = np.array([85, 88, 90, 79, 92, 84, 87])
group_b = np.array([78, 80, 83, 75, 82, 79, 81])

# Run Independent T-Test
# equal_var=False runs Welch's T-test (safer, does not assume equal variances)
stat, p = ttest_ind(group_a, group_b, equal_var=False)

print(f"T-Statistic: {stat:.4f}")
print(f"P-value: {p:.4f}")

