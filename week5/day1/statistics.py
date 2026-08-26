# 1 — Mean, Median, Variance, Standard Deviation
import pandas as pd
scores = [10, 30, 40, 50]
new_score = pd.Series(scores).mean()
print(new_score)


print(pd.Series(scores).median())
print(pd.Series(scores).max())
import numpy as np
print(np.array([10, 20, 30]).mean())

# variance
import pandas as pd 
import numpy as np
print(pd.Series(scores).var())
print(np.var(scores))

#standars devesion:
#Standard Deviation یا SD از Variance به دست می‌آید:
#
#Standard Deviation= 
#Variance
#​
print(np.std(scores))
print("\n")

import numpy as np
data = np.array([10, 30, 50, 70, 90])
print(np.mean(scores))
print(np.median(scores))
print(np.var(scores))
print(np.std(scores))




