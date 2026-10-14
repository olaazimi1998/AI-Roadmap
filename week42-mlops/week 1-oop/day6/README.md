# Week 1 - Day 6: Simple Banking System

A clean, beginner-friendly Python banking project demonstrating object-oriented programming, encapsulation, and inheritance.

## Project Overview

This folder contains a small banking system with:

- `BankAccount` for basic account operations
- `Savingaccount` as a savings account with interest
- `Costumer` to assign and display customer accounts
- `Bank` to manage registered customers
- `main.py` to demonstrate how the classes work together

## Features

- Create accounts with an owner, account number, and balance
- Deposit money safely, rejecting invalid amounts
- Withdraw money with balance checks
- Display account details
- Add interest to a savings account
- Link accounts to customers and display customer accounts
- Add customers to a bank instance

## Files

- `bank_account.py` - Defines `BankAccount` with deposit, withdraw, display, and balance access
- `saving_account.py` - Defines `Savingaccount`, which inherits from `BankAccount` and can add interest
- `costumer.py` - Defines `Costumer`, a container for one or more accounts
- `bank.py` - Defines `Bank`, which stores customers
- `main.py` - Example script showing how to create accounts, customers, and a bank

## How to Run

From the `week 1/day6` folder, run:

```bash
python main.py
```

## Notes

- The balance is kept as a private attribute inside `BankAccount` for better encapsulation.
- The project is a learning exercise in class design and working with objects.

Enjoy exploring the banking classes and extending them with new features!
