-- Active: 1789024196238@@127.0.0.1@3306


INSERT INTO products
(id, brand, model, price, ram_gb)
VALUES
(1, 'Apple', 'iPhone 15', 2990, 8),
(2, 'Samsung', 'S24', 2499, 8),
(3, 'Xiaomi', '14', 1999, 12),
(4, 'Google', 'Pixel 9', 2799, 12);


CREATE TABLE products (
    id INTEGER,
    brand TEXT,
    model TEXT,
    price INTEGER,
    ram_gb INTEGER
);



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


SELECT *
FROM products1;

SELECT id ,price
FROM products1
WHERE price > 2700


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


















