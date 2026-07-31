# Week 1 Day 4 — Polymorphism, Inheritance, and Account Behavior

This folder contains Python examples that demonstrate object-oriented programming principles using animals, family classes, employees, and bank accounts.

## Files

- `main.py` — runs the examples for polymorphism, method overriding, employee bonus calculations, and bank account operations.
- `models.py` — defines `Dog`, `Cat`, `Father`, and `Son` classes to show polymorphism and inheritance.
- `bank.py` — defines `BankAccount`, `SavingAccount`, and `CurrentAccount` for deposit and withdrawal behavior.
- `employee.py` — defines `Employee`, `Manager`, and `Developer` classes with different bonus calculations.

## What this day teaches

- Polymorphism: different objects (`Dog`, `Cat`) use the same method name (`speak`).
- Inheritance: `Son` extends `Father` and overrides the `read()` method.
- Method overriding: subclasses can extend or change parent behavior.
- Class design: create reusable base classes and specialized subclasses.
- Business rules: `SavingAccount` limits large withdrawals and both account types reuse base account logic.
- Role-specific behavior: managers and developers earn different bonus percentages.

## How to run

From this folder, run:

```bash
python main.py
```

Expected output includes:

- Animal sounds from `Cat` and `Dog`
- Reading behavior from `Father` and `Son`
- Employee names and bonus values
- Bank deposit and withdrawal messages

## Notes

This example is a practical introduction to using inheritance and polymorphism in Python while keeping code easy to extend and understand.