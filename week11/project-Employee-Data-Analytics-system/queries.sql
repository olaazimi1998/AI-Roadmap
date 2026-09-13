-- =========================================
-- QUERY 1
-- Show employees with their departments
-- =========================================

SELECT
    e.employee_id,
    e.first_name,
    e.last_name,
    d.department_name,
    e.salary
FROM employees e
JOIN departments d
    ON e.department_id = d.department_id;


-- =========================================
-- QUERY 2
-- Average salary for each department
-- =========================================

SELECT
    d.department_name,
    AVG(e.salary) AS average_salary
FROM employees e
JOIN departments d
    ON e.department_id = d.department_id
GROUP BY d.department_name;


-- =========================================
-- QUERY 3
-- Departments with average salary greater than 6000
-- =========================================

SELECT
    d.department_name,
    AVG(e.salary) AS average_salary
FROM employees e
JOIN departments d
    ON e.department_id = d.department_id
GROUP BY d.department_name
HAVING AVG(e.salary) > 6000;


-- =========================================
-- QUERY 4
-- Find the highest-paid employee
-- =========================================

SELECT
    first_name,
    last_name,
    salary
FROM employees
WHERE salary = (
    SELECT MAX(salary)
    FROM employees
);


-- =========================================
-- QUERY 5
-- Employees earning more than company average
-- =========================================

SELECT
    first_name,
    last_name,
    salary
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);


-- =========================================
-- QUERY 6
-- Rank all employees by salary
-- =========================================

SELECT
    first_name,
    last_name,
    salary,
    RANK() OVER (
        ORDER BY salary DESC
    ) AS salary_rank
FROM employees;


-- =========================================
-- QUERY 7
-- Rank employees inside each department
-- =========================================

SELECT
    e.first_name,
    e.last_name,
    d.department_name,
    e.salary,
    RANK() OVER (
        PARTITION BY e.department_id
        ORDER BY e.salary DESC
    ) AS department_rank
FROM employees e
JOIN departments d
    ON e.department_id = d.department_id;


-- =========================================
-- QUERY 8
-- Find the highest-paid employee in each department
-- =========================================

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


-- =========================================
-- QUERY 9
-- Show employees and the projects they work on
-- =========================================

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


-- =========================================
-- QUERY 10
-- Count employees and calculate total salary for each project
-- =========================================

SELECT
    p.project_name,
    COUNT(e.employee_id) AS employee_count,
    SUM(e.salary) AS total_employee_salary
FROM projects p
JOIN employee_projects ep
    ON p.project_id = ep.project_id
JOIN employees e
    ON ep.employee_id = e.employee_id
GROUP BY p.project_name
ORDER BY total_employee_salary DESC;