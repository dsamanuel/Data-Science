import numpy as np
from statsmodels.stats.contingency_tables import mcnemar

# Define the 2x2 table [[Both Yes, Yes->No], [No->Yes, Both No]]
table = np.array([[25, 5],
                  [15, 30]])

# Calculate McNemar's Test
# exact=True uses Binomial distribution (best for small samples, discordant cells < 25)
# exact=False uses Chi-Square distribution (requires continuity correction for medium samples)
result = mcnemar(table, exact=True)

# Output results
print(f"Statistic: {result.statistic}")
print(f"P-value: {result.pvalue}")

# Interpret findings
alpha = 0.05
if result.pvalue < alpha:
    print("Reject the null hypothesis: Significant change between groups.")
else:
    print("Fail to reject the null hypothesis: No significant change.")