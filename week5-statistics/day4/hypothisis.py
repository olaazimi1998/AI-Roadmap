#1. Define the question
#        ↓
#2. Define H₀
#        ↓
#3. Define H₁
#        ↓
#4. Choose α
#        ↓
#5. Collect data
#        ↓
#6. Run statistical test
#        ↓
#7. Get p-value
#        ↓
#8. Compare p-value with α
#        ↓
#9. Make conclusion


import pandas as pd 
import numpy as np
import scipy.stats as sp  # type: ignore[reportMissingTypeStubs]

group_a = [100, 105, 98, 102, 101]
group_b = [110, 115, 108, 112, 111]

# scipy-stubs may report this member as partially unknown to type checkers, so we
# narrow the inputs to NumPy arrays and suppress the specific diagnostic.
t_statistic, p_value = sp.ttest_ind( # type: ignore
    np.asarray(group_a, dtype=float),
    np.asarray(group_b, dtype=float),
)  # type: ignore[reportUnknownMemberType]

print("t-statistic:", t_statistic)
print("p-value:", p_value)
print(np.mean(group_a))
print(pd.Series(group_a).mean())

from scipy import stats # type: ignore

old = [100, 102, 98, 101, 99, 103, 97, 100]
new = [110, 112, 108, 115, 111, 109, 113, 114]

t_statistic, p_value = stats.ttest_ind( # type: ignore
    np.asarray(old, dtype=float),
    np.asarray(new, dtype=float),
)

print("t-statistic:", t_statistic)
print("p-value:", p_value)














