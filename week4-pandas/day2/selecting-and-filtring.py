import pandas as pd
data = { # type: ignore
    "name": ["saa", "ommid", "ali", "mina", "amir"],
    "age": [20, 30, 40, 50, 60],
    "city": ["sharja", "dubai", "diera", "abudabi", "raslkhaima"],
    "score": [60, 70, 80, 90,100]
    }


df = pd.DataFrame(data) # type: ignore
print(df)

print(df["name"])
print(df.columns.tolist())
#selecting several columns type two bracket
print(df[["name", "age", "city"]])

#selecting one row with loc (df.loc[row, column])
#if we write[0:2] it will write 3 columns or row
#work with lable we cant write the column names
#df.loc[0, "score"]
print(df.loc[0])
print(df.loc[0:2])
print(df.loc[0, "score"])

#selecting one row with iloc (df.iloc[row, column])
#if we write[0:2] it will write 2 columns or row
#not including last element
#df.iloc[0, 4]

print(df.iloc[0])
print(df.iloc[0:1])

result = df[df["score"] > 60]
print(result)
print(df[df["score"] > 70])

print(df[df["age"] > 25])
print(df[df["city"] == "dubai"])

data = { # type: ignore
    "name": ["sara", "ommid", "ali", "mina", "amir"],
    "age": [20, 30, 40, 50, 60],
    "city": ["sharja", "dubai", "diera", "abudabi", "raslkhaima"],
    "score": [60, 70, 80, 90,100]
    }


df = pd.DataFrame(data) # type: ignore
print(df)

print([df["age"] > 30])
print(df[df["score"] > 70])

print(df[df["score"] < 70])

print(df[df["city"] == "sharja"])
# & both condition must true
result =df[
    (df["age"] > 20) &
    (df["score"] > 70)
]
print(result)

# or |  one condition must be true
result = df[ 
    (df["city"] == "dubai") |
    (df["city"] == "sharja")
]
print(result)

#between
result = df[
    df["age"].between(20, 30)
]
print(result)

result = df[df["score"].between(4, 70)]
#isin best for selecting several element
result = df[
    df["city"].isin(["dubai", "sharja"])
]
print(result)
#filtering + selecting
result = df.loc[df["score"] > 70, ["name", "score"]
]
print(result)

result = df.loc[
    df["score"] > 60 , ["name", "score"]
]
print(result)


data = { # type: ignore
    "name": ["sara", "ali", "ahmed", "abidin"],
    "age": [20, 30, 40, 50],
    "city": ["paris","brazel", "japan", "dubai"],
    "score": [60, 70, 50, 90]
}

df = pd.DataFrame(data) # type: ignore
print(df)
print(df["name"])
print("\n")
print(df[["name", "score"]])

print("\n")
print(df.loc[1])

print("\n")
print(df.loc[df["name"] == "sara", "score"])

print(df.loc[df["age"] > 25])

print("\n")
print(df.loc[df["score"] > 85])

print("\n")
print(df.loc[df["city"] == "dubai"])
print("\n")
print(df[(df["age"] > 20) & (df["score"] < 70)])
print("\n")
print(df[(df["city"] == "dubai") |
       (df["city"] == "japan")])


print(df[(df["city"] == "dubai") | 
         (df["city"] == "paris")])



























