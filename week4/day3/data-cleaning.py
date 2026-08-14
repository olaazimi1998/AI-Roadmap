import pandas as pd

data = { # type: ignore
    "name": ["Ali", "Sara", "Amir", "Mina", "Omar"],
    "age": [20, 25, None, 22, 28],
    "score": [80, None, 75, 88, 1000]
}

df = pd.DataFrame(data) # type: ignore

print(df)





#NAN mean 
#Not a Number / missing value
print(df.isna())
print(df.isnull())

#number of NAN in each column
print(df.isna().sum())

#is there NAN?
print(df.isna().any())

#cleaning row of NAN
print(df.dropna())
clean_df = df.dropna()
print(clean_df)

#cleaning one column of NAN
print(df.dropna(subset=["age"]))
print(df.dropna(subset=["name"]))

#filing NAN with mean and median
mean_age = df["age"].mean()
print(mean_age)
df["age"] = df["age"].fillna(mean_age)
print(df["age"])
print(df)

median_age = df["score"].median()
df["score"] = df["score"].fillna(median_age)
print(df["score"])
print(df)

mean_score = df["score"].mean()
df["score"] = df["score"].fillna(mean_score) # type: ignore
print(df)
#duplicate
data = {  # type: ignore
    "name": ["ali", "sara", "ali"],
    "age": [20, 40, 20]
}

df = pd.DataFrame(data) # type: ignore
print(df)

print(df.duplicated())

#delete duplicate

df = df.drop_duplicates()
print(df)

data = {
    "age": ["20", "40", "50"]
}

df = pd.DataFrame(data)
print(df)

print(df.info())

#changing datatype:
df["age"] = df["age"].astype(int)
print(df)
print(df.info())

# pd.to_numeric() change unknown to Nan then to median
data = {
    "score": ["80", "90", "unknown", "75"]
}

df = pd.DataFrame(data)
print(df)
df["score"] = pd.to_numeric(df["score"], errors="coerce")
print(df)
median_score = df["score"].median()
df["score"] = df["score"].fillna(median_score)
print(df)

#cleaning text

data = {
    "name": ["Ali ", " Sara ", " Amir"]
}

df = pd.DataFrame(data)
print(df)

df["name"] = df["name"].str.strip()
print(df)

#uppercase
df["name"] = df["name"].str.upper()
print(df)

#lowercase
df["name"] = df["name"].str.lower()
print(df)


data = {
    "name": [" Ali ", "Sara ", " Amir", "Mina"]
}

df = pd.DataFrame(data)
# replacing text
df["name"] = df["name"].str.replace("Mina", "MINA")
print(df)


import pandas as pd

data = {  # type: ignore
    "name":[" ali", "sara ", "amir", " mina", "ali"],
    "age":["20", "30", "40", None, "23"],
    "score":["80", "70", "66", "unknown", "56"]

}
df = pd.DataFrame(data) # type: ignore
print("Orignal")
print(df)

#  Cleaning names 
df["name"] = df["name"].str.strip()

# Convert age to numric
df["age"] = pd.to_numeric(df["age"], errors="coerce")

# Converting score to numeric
df["score"] = pd.to_numeric(df["score"], errors="coerce")

# Fill missing age
df["age"] = df["age"].fillna(df["age"].median())

#Filling missing score
df["score"] = df["score"].fillna(df["score"].median())

#remove duplicates
df = df.drop_duplicates()

print("\nCleaned:")
print(df)


#exercise:

import pandas as pd

data = {
    "name": [" Ali ", "Sara", "Ali", "Amir ", "Mina"],
    "age": [20, None, 20, 30, None],
    "score": [80, 90, 80, None, 88],
    "city": ["Dubai", "Sharjah", "Dubai", "Dubai", None]
}

df = pd.DataFrame(data)

print(df.isna())
print(df.isna().sum())
print(df.isna().any())
print("\n")
df["name"] = df["name"].str.strip()
print(df)
print("\n")
print(df.duplicated())
df = df.drop_duplicates()
print(df)

df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["score"] = pd.to_numeric(df["score"], errors="coerce")
df["age"] = df["age"].fillna(df["age"].median())
df["score"] = df["score"].fillna(df["score"].median())
df["city"] = df["city"].fillna("unknown")
print(df.info())
print(df.isna().sum())
print(df)
# Find missing values
df.isna()

# Count missing values
df.isna().sum()

# Check if any missing values exist
df.isna().any()

# Remove rows with NaN
df.dropna()

# Remove based on specific column
df.dropna(subset=["age"])

# Fill NaN
df["age"].fillna(25)

# Fill with mean
df["age"].fillna(df["age"].mean())

# Fill with median
df["age"].fillna(df["age"].median())

# Find duplicates
df.duplicated()

# Remove duplicates
df.drop_duplicates()

# Convert to number
pd.to_numeric(df["score"], errors="coerce")

# Remove spaces
df["name"].str.strip()

# Lowercase
df["name"].str.lower()

# Uppercase
df["name"].str.upper()