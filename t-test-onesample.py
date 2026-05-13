import scipy.stats as stats

# Weights of potato chip bags from a factory line
weights = [10.2, 10.1, 9.9, 10.0, 10.3, 9.8, 10.1]
avgs = sum(weights) / len(weights)
print(f"Average weight: {avgs:.2f} grams")
expected_mean = 10.0

# Run one-sample t-test
t_stat, p_val = stats.ttest_1samp(weights, expected_mean)

print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_val:.4f}")