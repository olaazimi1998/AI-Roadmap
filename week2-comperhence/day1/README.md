# Week 2 Day 1 — Python List Comprehensions

This folder contains Python examples that demonstrate how to use list comprehensions to build, transform, and filter lists in a compact and readable way.

## What is a list comprehension?

A list comprehension is a concise way to create a new list by applying an expression to each item in an existing iterable.

Basic form:

```python
new_list = [expression for item in iterable]
```

With conditionals:

```python
filtered = [expression for item in iterable if condition]
```

And with an inline `if/else` expression:

```python
mapped = [expr_if_true if condition else expr_if_false for item in iterable]
```
```

## Examples in `list-comperhension.py`

- Create a list of integers:
  - `numbers = [i for i in range(10)]`
- Generate square values:
  - `numbers = [i ** 2 for i in range(1, 20)]`
- Generate cube values:
  - `numbers = [i ** 3 for i in range(1, 20)]`
- Add a constant to each value:
  - `numbers = [i + 4 for i in range(6, 9)]`
- Filter even numbers:
  - `evens = [i for i in range(20) if i % 2 == 0]`
- Filter numbers divisible by 3:
  - `odds = [i for i in range(20) if i % 3 == 0]`
- Transform strings to uppercase and lowercase:
  - `upper_names = [name.upper() for name in names]`
  - `lower_names = [name.lower() for name in names]`
- Compute word lengths:
  - `lengths = [len(word) for word in words]`
- Combine expression and filter:
  - `numbers = [i ** 2 for i in range(20) if i % 2 == 0]`
- Use inline conditional expressions:
  - `numbers = [i ** 4 if i % 2 == 0 else -i for i in range(10)]`
- Build nested lists (a matrix):
  - `matrix = [[i * j for j in range(6)] for i in range(7)]`
- Filter adult ages:
  - `adults = [age for age in ages if age >= 18]`
- Convert probability predictions into classes:
  - `classes = [1 if p > 0.5 else 0 for p in Predictions]`

## How to run

Open a terminal in this folder and run:

```powershell
python list-comperhension.py
```

## Learning goals

- Understand how list comprehensions simplify loops.
- Practice filtering values with `if` conditions.
- Use inline `if/else` expressions for conditional mapping.
- Create nested list comprehensions for multi-dimensional data.

## Notes

- List comprehensions are more concise than equivalent `for` loops.
- They are ideal for transforming or filtering collections in one statement.
- Avoid making them too complex; if logic becomes hard to read, use a normal loop.
