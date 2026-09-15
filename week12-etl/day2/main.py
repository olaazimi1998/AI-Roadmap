from models import Employee
from etl import extract, validate


print("------")

data = extract()
valid_employees, invalid_rows = validate(data)

print("Valid employees")
print("-----------")
for employee in valid_employees:
    print(employee)

print("Invalid Data")
print("----------")
for row in invalid_rows:
    print(row)

print("Raw data:")
print(data)