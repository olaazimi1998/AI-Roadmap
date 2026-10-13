# Week 4 — Day 1: Pandas Basics

This folder contains a small example demonstrating basic pandas usage in Python.

Files
- `Pandas Basics + D.pyataFrame.py`: example script showing `Series` and `DataFrame` creation and common operations.

Quick start

1. Create a Python environment (optional):

	python -m venv .venv
	.venv\Scripts\activate

2. Install dependencies:

	pip install pandas

3. Run the example:

	python "Pandas Basics + D.pyataFrame.py"

What it demonstrates
- Creating `pd.Series` and `pd.DataFrame` from native Python structures.
- Inspecting data with `head()`, `tail()`, `info()`, `describe()`.
- Accessing metadata: `columns`, `shape`.
- Selecting columns and simple aggregations: `mean()`, `max()`, `min()`.

Notes
- The script prints `df.info()` and other outputs to the console for learning purposes.
- If you see `<built-in method info of DataFrame object at ...>` in output, ensure the script calls `df.info()` (with parentheses) rather than printing `df.info`.

License
- Educational sample — do whatever you like with it.

