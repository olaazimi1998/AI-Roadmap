
CREATE TABLE products11(
    id INTEGER,
    brand TEXT,
    model TEXT,
    price INTEGER,
    ram_gb INTEGER
);

INSERT INTO products11
(id, brand, model, price, ram_gb)
VALUES
(1, 'Apple', 'iPhone 15', 2990, 8),
(2, 'Samsung', 'S24', 2499, 8),
(3, 'Xiaomi', '14', 1999, 12),
(4, 'Google', 'Pixel 9', 2799, 12);

SELECT *
FROM products11
WHERE price >= 1990
AND brand = 'Apple'

SELECT *
FROM products11
WHERE  NOT price > 2000
OR brand = 'Xiaomi'

SELECT *
FROM products11
ORDER BY price ASC;
#sort from low to high

SELECT *
FROM products11
ORDER BY price DESC;
# sort from hight to low

SELECT *
FROM products11
LIMIT 3

# SELECT columns
#FROM table
#WHERE condition
#ORDER BY COLUMN
#LIMIT row_number;

