# One column
df["name"]

# Multiple columns
df[["name", "score"]]

# One row
df.loc[0]

# One cell
df.loc[0, "score"]

# Position
df.iloc[0, 2]

# Greater than
df[df["score"] > 85]

# Less than
df[df["score"] < 85]

# Equal
df[df["city"] == "Dubai"]

# AND
df[(df["age"] > 20) & (df["score"] > 80)]

# OR
df[(df["city"] == "Dubai") | (df["city"] == "Sharjah")]

# Multiple values
df[df["city"].isin(["Dubai", "Sharjah"])]

# Range
df[df["age"].between(20, 25)]

# Filter + select columns
df.loc[df["score"] > 85, ["name", "score"]]