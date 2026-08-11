import pandas as pd 

#series is a column of data:
ages = pd.Series([20,30,40,50])
print(ages)

numbers = pd.Series([20,30,40,50,80])
print(numbers)

#  DataFrame is like a table excel file
data = {
    "name": ["sara", "ali", "amir" ] , 
    "age": [20, 39, 40], 
    "score": [90, 88, 78]
}

df = pd.DataFrame(data)
print(df)

#show two row of first
print(df.head(2))

#show two row of last
print(df.tail(1))

# data of dataframe count row, column, name of columns , data type, count data of non_null.
print(df.info())

#describe 
print(df.describe())

#name of columns
print(df.columns)

#number of row and column :
print(df.shape)

print(pd.DataFrame(data))

print(df.head(1))
print(df.tail(2))
print(df.shape)
print(df.describe())
print(df.info)
print(df.columns)
#change the index to list
print(df.columns.tolist())

#selecting the column
print(df["name"])
print(df["age"])

#calculate the mean of age column
print(df["age"].mean())
print(df["score"].max())
print(df["score"].min())








