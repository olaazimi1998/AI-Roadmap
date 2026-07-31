# Week 1 Day 5 — Abstract Classes and Polymorphism

This folder contains Python examples showing how to use abstract base classes, polymorphism, and consistent interfaces across different types.

## Files

- `main.py` — runs the examples for books, machine learning models, and payment methods.
- `models.py` — defines the `Book` abstract base class and the concrete `Math` subclass.
- `mlmodel.py` — defines the `MLModel` abstract base class and concrete implementations for `LinearRegression` and `DecisionTree`.
- `payment.py` — defines the `Payment` abstract base class and concrete implementations for `Paypal` and `Creditcard`.

## Concepts demonstrated

- `ABC` and `abstractmethod` from Python's `abc` module
- Abstract base classes for shared behavior contracts
- Polymorphism with different objects implementing the same methods
- Separate implementation and runtime usage

## How to run

From this folder, run:

```bash
python main.py
```

Expected output:

- A study message from `Math`
- Training and prediction messages for both ML models
- Payment messages for PayPal and credit card

## Notes

This day shows how abstract interfaces make it easy to work with multiple implementations while keeping the calling code clean and simple.