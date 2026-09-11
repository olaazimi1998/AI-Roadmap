# Week 2 Day 3 — Python Generators and File Iteration

This folder contains Python examples that demonstrate generator functions, generator expressions, and simple file reading with iterators.

## Files

- `genarators.py` — contains examples of generator functions, generator expressions, and file-reading generators.
- `dataset.csv` — sample CSV data used by the CSV reader examples.
- `number.txt` — sample numeric data used by the file-reading examples.

## What this day teaches

- How to define and use generator functions with `yield`.
- How generator functions produce values lazily on demand.
- How to iterate through generator results using `for` loops and `next()`.
- How to build custom iterators for filtering values from files.
- How to parse CSV data line-by-line using generators.

## Key examples in `genarators.py`

- `list_numbers()` — returns a normal Python list.
- `test()` — demonstrates that only the first `return` is executed.
- `numbers()` — yields values with a simple generator function.
- `count()` — yields a range of values from 1 to 10.
- `squares(n)` — yields computed values inside a generator.
- `even_numbers(limit)` — yields even numbers within a limit.
- `read_file(filename)` — reads a text file line by line and yields trimmed lines.
- `csv_reader(file_name)` — reads a CSV-like file and yields comma-split rows.
- A filtered `read_file` example that yields numbers greater than 50.

## How to run

Open a terminal in this folder and run:

```powershell
python genarators.py
```

## Notes

- Generator functions are useful for processing large sequences without building the whole list in memory.
- The file-reading examples show how to iterate safely over file contents.
- The CSV reader example uses simple string splitting and is intended for small sample data.
