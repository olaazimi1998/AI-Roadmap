CREATE TABLE department (
    department_id INTEGER PRIMARY KEY,
    department_name VARCHAR(100) Not NULL
);

CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    department_id INTEGER,
    salary DECIMAL(10, 2),
    hire_date DATE,
    
    FOREIGN KEY (department_id)
        REFERENCES department(department_id)
);

CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    budget DECIMAL(12, 2)
);

CREATE TABLE employee_projects (
    employee_id INTEGER,
    project_id INTEGER,

    PRIMARY KEY (employee_id, project_id),

    FOREIGN KEY (employee_id)
        REFERENCES employees(employee_id),

    FOREIGN KEY (project_id)
        REFERENCES projects(project_id)

);

#PRIMARY KEY
#
#Uniquely identifies a row.
#
#employee_id INTEGER PRIMARY KEY
#
#Two employees cannot have the same employee_id.
#
#FOREIGN KEY
#
#Connects tables.
#
#department_id INTEGER
#REFERENCES departments(department_id)
#
#This means an employee belongs to a department.



