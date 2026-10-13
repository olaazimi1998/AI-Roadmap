from etl import extract, transform, validate, load
from database import create_database, get_employees
from logger import logger


print("================================")
print("       EMPLOYEE ETL PIPELINE")
print("================================")


logger.info("========== PIPELINE STARTED ==========")


# Create database
create_database()


# 1. EXTRACT
data = extract()


if data is None:

    print("Extraction failed.")
    print("Check logs/etl.log")

else:

    print("\nRAW DATA")
    print("--------")
    print(data)


    # 2. TRANSFORM
    data = transform(data)


    print("\nCLEAN DATA")
    print("----------")
    print(data)


    # 3. VALIDATE
    valid_employees, invalid_rows = validate(data)


    print("\nVALID EMPLOYEES")
    print("----------------")

    for employee in valid_employees:
        print(employee)


    print("\nINVALID ROWS")
    print("------------")

    for row in invalid_rows:
        print(row)


    # 4. LOAD
    load(valid_employees)


    # 5. READ DATABASE
    print("\nDATABASE DATA")
    print("-------------")

    employees = get_employees()

    for employee in employees:
        print(employee)


logger.info("========== PIPELINE FINISHED ==========")


print("\n================================")
print("       PIPELINE COMPLETED")
print("================================")