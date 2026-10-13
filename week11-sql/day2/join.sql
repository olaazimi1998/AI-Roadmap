# INNER JOIN returns only rows that exist in both tables.
#SELECT
#    students.name,
#    courses.course_name
#FROM students
#INNER JOIN courses
#ON students.course_id = courses.id;

CREATE TABLE products1 (
    id INTEGER,
    brand TEXT,
    model TEXT,
    price INTEGER,
    ram_gb INTEGER
);


INSERT INTO products1
(id, brand, model, price, ram_gb)
VALUES
(1, 'Apple', 'iPhone 15', 2990, 8),
(2, 'Samsung', 'S24', 2499, 8),
(3, 'Xiaomi', '14', 1999, 12),
(4, 'Google', 'Pixel 9', 2799, 12);


#join
SELECT 
products1.price,
students.age
FROM students
INNER join products1
on products1.id = students.id;

CREATE TABLE students (
    id INTEGER,
    name TEXT,
    age INTEGER,
    grade INTEGER
);
INSERT INTO students (id, name, age, grade)
VALUES (1, 'Ali', 20, 90);

INSERT INTO students (id, name, age, grade)
VALUES (2, 'Sara', 21, 95);

INSERT INTO students (id, name, age, grade)
VALUES (3, 'John', 19, 80);

SELECT *
FROM students;

SELECT name, grade
FROM students
WHERE grade >= 90;

CREATE TABLE employees (
    employee VARCHAR(50),
    department VARCHAR(50),
    salary INT
);

INSERT INTO employees (employee, department, salary)
VALUES
('Ali', 'IT', 5000),
('Sara', 'IT', 7000),
('John', 'HR', 4000),
('Mary', 'HR', 6000);

SELECT *
FROM employees
WHERE department = 'IT';

SELECT
    employee,
    department,
    salary,
    AVG(salary) OVER (
        PARTITION BY department
    ) AS department_average
FROM employees;


SELECT
    department,
    AVG(salary)
FROM employees
GROUP BY department;

SELECT
employee,
salary,
RANK() OVER (
    ORDER BY salary DESC
) AS salary_rank
FROM employees;

CREATE TABLE employees1 (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER
);
INSERT INTO employees1 (name, department, salary)
VALUES
('Ali', 'IT', 5000),
('Sara', 'IT', 7000),
('John', 'HR', 4000),
('Mary', 'HR', 6000),
('David', 'IT', 8000);

SELECT
    name,
    department,
    salary,
    AVG(salary) OVER (
        PARTITION BY department
    ) AS department_average
FROM employees1;


