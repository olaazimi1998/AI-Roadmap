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