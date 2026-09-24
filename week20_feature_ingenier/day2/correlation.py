import pandas as pd
data = {
    "age": [20, 25, 30, 35, 40],
        "experience": [1, 3, 7, 10, 15],
        "salary": [2000, 3000, 5000, 7000, 10000],
        "hours_worked": [40, 40, 45, 45, 50]
}

df = pd.DataFrame(data)
print(df)

correlation = df.corr()

print("\nCorrelation Matrix:")
print(correlation)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "age": [20, 25, 30, 35, 40],
    "experience": [1, 3, 7, 10, 15],
    "salary": [2000, 3000, 5000, 7000, 10000],
    "hours_worked": [40, 40, 45, 45, 50]
}

df = pd.DataFrame(data)

correlation = df.corr()

print(correlation)

sns.heatmap(
    correlation,
    annot=True
)

plt.title("Correlation Matrix")

plt.show()