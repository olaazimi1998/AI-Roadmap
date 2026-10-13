


#1. What is an Index?
#
#Imagine you have a book with 1,000 pages.
#
#You want to find:
#
#“Where is the word Python?”
#
#Without an index, you might check page by page. 🐌
#
#With the book's index, you can find it quickly. ⚡
#
#A SQL index works similarly.

1. What is an Index?

Imagine you have a book with 1,000 pages.

You want to find:

“Where is the word Python?”

Without an index, you might check page by page. 🐌

CREATE TABLE employees4 (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER
);

INSERT INTO employees4 (name, department, salary)
VALUES
('Ali', 'IT', 5000),
('Sara', 'IT', 7000),
('John', 'HR', 4000),
('Mary', 'HR', 6000),
('David', 'IT', 8000);


CREATE INDEX idx_salary ON employees4 (salary);
SELECT * FROM employees4 where salary > 5000;


