
import sqlite3

DATABASE_PATH = r"C:\Users\olaaz\Documents\AI Roadmap\week12-etl\day3\data\employees.db"

def create_database():
    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        department TEXT,
        salary INTEGER
        )""")

    connection.commit()
    connection.close()

def insert_employee(employee):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO employees (name, age, department, salary)
        VALUES (?, ?, ?, ?)
    """, (employee.name, employee.age, employee.department, employee.salary))

    connection.commit()
    connection.close()

def get_employees():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, age, department, salary
        FROM employees
    """)
    employees = cursor.fetchall()

    connection.close()
    return employees
