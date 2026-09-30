import pandas as pd

data = {
    "hours_studied": [1, 2, 3, 4, 5],
    "exam_score": [50, 55, 65, 70, 80]
}

df = pd.DataFrame(data)

print(df.corr())

from scipy.stats import ttest_ind
group_a = [70, 72, 68, 75, 71]
group_b = [80, 82, 79, 85, 81]

result = ttest_ind(group_a, group_b)
print("t-statistic:", result.statistic)
print("p-value:", result.pvalue)

if result.pvalue < 0.05:
    print("Evidence against the null hypothesis.")
else:
    print("Not enough evidence against the null hypothesis.")