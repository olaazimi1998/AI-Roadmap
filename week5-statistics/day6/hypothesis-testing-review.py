#1. The Big Picture
#Imagine you're working as an AI Engineer for an online store.
#
#You have this question:
#
#"Did changing the website design increase sales?"
#
#You collect data:

old_design = [102, 98, 105, 110, 95, 100, 97, 103]
new_design = [115, 120, 118, 125, 119, 122, 117, 121]

# null hypothesis
#H₀: New design does NOT increase sales.

#alternative hypothesis
#H₁: New design DOES increase sales.

#H₀ = nothing happened
#H₁ = something happened

#p-value
#This is one of the most important concepts in Statistics.
#
#The p-value helps us determine how surprising our observed result would be if the null hypothesis were true.
#
#A common threshold is

#α = 0.05

# then
#p-value < 0.05
 #       ↓
#Reject H₀ # type: ignore

#while:
# p-value >= 0.05
 #       ↓
# not reject H₀
#

from scipy.stats import ttest_ind # type: ignore

old_design = [102, 98, 105, 110, 95, 100, 97, 103]
new_design = [115, 120, 118, 125, 119, 122, 117, 121]

t_stat, p_value = ttest_ind(
    old_design,
    new_design
)

print("t-statistic:", t_stat)
print("p-value:", p_value)


from scipy.stats import ttest_ind # type: ignore

old_design = [102, 98, 105, 110, 95, 100, 97, 103]
new_design = [115, 120, 118, 125, 119, 122, 117, 121]

t_stat, p_value = ttest_ind(
    old_design,
    new_design
)

print("t-statistic:", t_stat)
print("p-value:", p_value)


import numpy as np

hours_studied = np.array([1, 2, 3, 4, 5, 6])
exam_score = np.array([50, 55, 65, 70, 80, 90])

correlation = np.corrcoef(
    hours_studied,
    exam_score
)[0, 1]

print(correlation)

#             DATA
#               ↓
#       ┌───────┴────────┐
#       ↓                ↓
# Descriptive        Distribution
# Statistics              ↓
#       ↓              Normal /
# Mean                  Poisson
# Median
# Variance
# Std
#       ↓
#   Correlation
#       ↓
#Correlation ≠ Causation
#       ↓
#Hypothesis Testing
#       ↓
#     t-test
#       ↓
#    p-value
#       ↓
# Statistical Decision



import pandas as pd
np.random.seed(42)

control_sales = np.random.normal(
    loc=100,
    scale=15,
    size=100
)

treatment_sales = np.random.normal(
    loc=110,
    scale=15,
    size=100
)
print(control_sales[:10])
print(treatment_sales[:10])


control_df = pd.DataFrame({
    "group": "control",
    "sales": control_sales
})

treatment_df = pd.DataFrame({
    "group": "treatment",
    "sales": treatment_sales
})

df = pd.concat(
    [control_df, treatment_df],
    ignore_index=True
)

print(df)











