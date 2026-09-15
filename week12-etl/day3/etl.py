import pandas as pd
from pydantic import ValidationError
from models import Employee
from database import insert_employee

def extract():
    try:
        return pd.read_csv(r"C:\Users\olaaz\Documents\AI Roadmap\week12-etl\day3\data\employees.csv")
    except (FileNotFoundError, pd.errors.ParserError) as error:
        return None


def transform(data):
    data = data.copy()
    data.columns = data.columns.str.strip().str.lower()

    for column in ["name", "department"]:
        data[column] = data[column].astype("string").str.strip()

    for column in ["age", "salary"]:
        data[column] = pd.to_numeric(data[column], errors="coerce")

    return data

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


def load(valid_employees):

    for employee in valid_employees:
        insert_employee(employee)