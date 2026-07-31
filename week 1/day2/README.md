# Week 1 Day 2 — Encapsulation and Data Protection

This folder contains Python examples that focus on encapsulation, private attributes, getters/setters, and property access control.

## Files

- `main.py` — runs the examples showing account operations, private fields, and property behavior.
- `models.py` — defines several classes that demonstrate encapsulation in different ways.

## What this day teaches

- How to keep object state private using name mangling (`__attribute`).
- How to use getters and setters to control access to internal data.
- How Python `@property` and `@<property>.setter` decorators create safe attribute access.
- How encapsulation helps prevent invalid data and improves object integrity.

## How to run

From this folder, run:

```bash
python main.py
```

Expected output includes:

- account deposits and withdrawals with balance updates
- a private pen name example
- school age access through getter/setter methods
- read-only balance access using `@property`
- temperature validation via property assignment
- balance protection with setter rules

## Notes

This example set is designed to show how objects can manage their own data safely while still exposing clean interfaces to callers.
