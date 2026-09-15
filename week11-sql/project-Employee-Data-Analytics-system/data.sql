INSERT INTO department
(department_id, department_name)
VALUES
(1, 'IT'),
(2, 'HR'),
(3, 'Finance'),
(4, 'marketing');
INSERT INTO employees
(employee_id, first_name, last_name, department_id, salary, hire_date)
VALUES
(1, 'Ali', 'Ahmadi', 1, 5000, '2022-01-15'),
(2, 'Sara', 'Karimi', 1, 7000, '2021-03-20'),
(3, 'John', 'Smith', 2, 4000, '2023-06-10'),
(4, 'Mary', 'Jones', 2, 6000, '2020-08-12'),
(5, 'David', 'Brown', 3, 8000, '2019-04-25'),
(6, 'Emma', 'Wilson', 3, 7500, '2021-11-05'),
(7, 'Omar', 'Hassan', 4, 4500, '2022-07-18'),
(8, 'Lina', 'Khan', 4, 6500, '2020-02-14'),
(9, 'James', 'Taylor', 1, 9000, '2018-09-30'),
(10, 'Sophia', 'Martin', 2, 5500, '2022-12-01');


INSERT INTO projects
(project_id, project_name, budget)
VALUES
(1, 'AI Platform', 100000),
(2, 'Website Redesign', 50000),
(3, 'Data Pipeline', 80000),
(4, 'Marketing Campaign', 40000);

INSERT INTO employee_projects
(employee_id, project_id)
VALUES
(1, 1),
(2, 1),
(5, 1),
(6, 3),
(9, 3),
(3, 2),
(4, 2),
(7, 4),
(8, 4),
(10, 2);

# Show all employees with departments
SELECT 
e.employee_id,
e.first_name,
e.last_name,
d.department_name,
e.salary
FROM employees e 
JOIN department d 
    ON e.department_id = d.department_id;
    
#Average salary by departments
SELECT
    d.department_name,
    AVG(e.salary) AS average_salary
    FROM employees e
    JOIN department d
    ON e.department_id = d.department_id
GROUP BY d.department_name;

# Department with average salary  > 6000
SELECT
    d.department_name,
    AVG(e.salary) AS average_salary
FROM employees e
JOIN department d
    ON e.department_id = d.department_id
GROUP BY d.department_name
HAVING AVG(e.salary) > 6000;

#
#mportant difference
#WHERE filters rows.
#
#HAVING filters groups.
#
#Remember:
#
#WHERE  → before GROUP BY
#HAVING → after GROUP BY

# Highest paid employee
SELECT
    first_name,
    last_name,
    salary
FROM employees
WHERE salary = (
    SELECT MAX(salary)
    FROM employees
);


SELECT MAX(salary)
FROM employees

# Employees earning more then average
SELECT
    first_name,
    last_name,
    salary
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);

# Employee rank by salary

SELECT
    first_name,
    last_name,
    salary,
    RANK() OVER (
        ORDER BY salary DESC 
    ) AS salary_rank
    FROM employees;

# Rank employee inside each department
SELECT
    e.first_name,
    e.last_name,
    d.department_name,
    e.salary,

    RANK() OVER (
        PARTITION BY e.department_id
        ORDER BY e.salary ASC
    ) AS department_rank

FROM employees e
JOIN department d
    ON e.department_id = d.department_id;

 #Highest Paid Employee in Each Department
WITH ranked_employees AS (

    SELECT
        e.*,

        RANK() OVER (
            PARTITION BY department_id
            ORDER BY salary DESC
        ) AS salary_rank

    FROM employees e
)

SELECT
    first_name,
    last_name,
    department_id,
    salary
FROM ranked_employees
WHERE salary_rank = 1;

# Employees and Their Projects
WITH ranked_employees AS (

    SELECT
        e.*,

        RANK() OVER (
            PARTITION BY department_id
            ORDER BY salary DESC
        ) AS salary_rank

    FROM employees e
)

SELECT
    first_name,
    last_name,
    department_id,
    salary
FROM ranked_employees
WHERE salary_rank = 1;


# Employees and Their Projects

SELECT
    e.first_name,
    e.last_name,
    p.project_name,
    p.budget
FROM employees e
JOIN employee_projects ep
    ON e.employee_id = ep.employee_id
JOIN projects p
    ON ep.project_id = p.project_id;


 #Project Employee Count and Total Salary
#This is our final complex query.

SELECT
    e.first_name,
    e.last_name,
    p.project_name,
    p.budget
FROM employees e
JOIN employee_projects ep
    ON e.employee_id = ep.employee_id
JOIN projects p
    ON ep.project_id = p.project_id;