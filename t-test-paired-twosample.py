from scipy.stats import ttest_rel
import numpy as np
import pandas as pd
from scipy import stats

# Sample continuous data for paired observations
pre_test = np.array([72, 75, 68, 80, 74, 71])
post_test = np.array([78, 81, 72, 85, 76, 79])

# Run Paired T-Test
stat, p = ttest_rel(pre_test, post_test)

print(f"T-Statistic: {stat:.4f}")
print(f"P-value: {p:.4f}")



# 1. Prepare data (Example: Reaction times in seconds Before and After caffeine)
data = pd.DataFrame({
    'Before': [2.5, 3.1, 2.8, 3.4, 2.9, 3.0, 3.2, 2.7, 3.3, 2.9],
    'After':  [2.1, 2.7, 2.9, 3.0, 2.5, 2.6, 3.1, 2.4, 2.8, 2.7]
})

# 2. Calculate the differences (The paired t-test analyzes this distribution)
data['Difference'] = data['After'] - data['Before']

# 3. Assumption Check: Normality of the differences (Shapiro-Wilk Test)
# H0: The differences are normally distributed.
shapiro_stat, shapiro_p = stats.shapiro(data['Difference'])
print(f"Normality Test (Shapiro-Wilk): p-value = {shapiro_p:.4f}")
if shapiro_p < 0.05:
    print("WARNING: Differences are not normally distributed. Consider Wilcoxon Signed-Rank test.")
else:
    print("SUCCESS: Normality assumption met.")

# 4. Execute the Paired t-Test
# H0: The mean difference between the two conditions is zero.
t_stat, p_value = stats.ttest_rel(data['After'], data['Before'])
print(f"\nPaired t-test Results:")
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value:     {p_value:.4f}")

# 5. Calculate Effect Size (Cohen's d for paired samples)
mean_diff = data['Difference'].mean()
std_diff = data['Difference'].std(ddof=1)
cohens_d = mean_diff / std_diff
print(f"Cohen's d:   {cohens_d:.4f}")
