import pandas as pd
from pydantic import ValidationError
from models import Employee


def extract():
    return pd.read_csv(r"C:\Users\olaaz\Documents\AI Roadmap\week12-etl\day2\data\employees.csv")

def validate(data):

    valid_employees = []
    invalid_rows = []

    for index, row in data.iterrows():

        try:

            employee = Employee(
                name=row["name"].strip(),
                age=row["age"],
                department=row["department"].strip(),
                salary=row["salary"]
            )

            valid_employees.append(employee)

        except ValidationError as error:

            invalid_rows.append({
                "row": index,
                "error": str(error)
            })

    return valid_employees, invalid_rows