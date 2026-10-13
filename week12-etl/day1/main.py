from etl import extract, transform, load

data = extract()

print("raw data:")
print(data)

data = transform(data)
print("Clean data:")
print(data)
load(data)
print("ETL complete")