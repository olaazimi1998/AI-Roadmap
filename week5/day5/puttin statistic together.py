import pandas as pd
data = { # type: ignore
    "add_campaign": [
        "old", "old","old", "old", "old",
        "new", "new", "new", "new", "new"
    ],
    
        "sales":[
            100, 105, 98, 102, 101,
            115, 120, 112, 118, 121
        ]
    
}
df = pd.DataFrame(data) # type: ignore
print(df)

print(df.head())
print(df.info())
print(df.describe())

print(df.groupby("add_campaign")["sales"].mean())
print(df.groupby("add_campaign")["sales"].median())

print(df.groupby("add_campaign")["sales"].std())

df["ad_spend"] = [
    20, 21, 19, 20, 22,
    30, 32, 29, 31, 33
]

print(df[["ad_spend", "sales"]].corr())

from scipy import stats # type: ignore
old_sales = df[
    df["add_campaign"] == "old"
]["sales"]

new_sales = df[ 
df["add_campaign"] == "new"
]["sales"]

result = stats.ttest_ind( # type: ignore
    old_sales,
    new_sales
)
print("Statistic:" , result.statistic) # type: ignore
print("p-value:", result.pvalue) # type: ignore


#p-value = 0.001
#0.001 < 0.05
#Reject H₀



















