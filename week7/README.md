# Week 7 - Probability, Calculus, and Optimization

## Overview
This week focuses on the mathematical foundations behind machine learning and intelligent systems. The main themes are probability, Bayes' theorem, calculus, derivatives, and gradient descent.

The goal is to build a strong understanding of how data-driven models estimate uncertainty, optimize decisions, and learn from examples.

## Weekly Learning Goals
- Understand basic probability and conditional probability
- Learn and apply Bayes' theorem
- Explore probability rules used in machine learning
- Understand derivatives and the concept of a gradient
- Learn how gradient descent minimizes error in models
- Apply these ideas to a practical fraud detection project

## Folder Structure

```text
week7/
├── README.md
├── day1/
│   └── probability
├── day2/
│   └── bayes-therem.P
├── day3/
│   └── probabiblity
├── day4/
│   └── gradiant-derivate.PY
├── day5/
│   └── chain_rule.py
├── day6/
│   └── probability-calculusforml.py
├── day7/
│   └── big-weekly-project.py
│   └── final-review
├── week7-fraud_detection/
│   ├── README.md
│   ├── requirements.txt
│   ├── data/
│   │   └── transactions.csv
│   ├── notebooks/
│   │   └── fraud_detection.ipynb
│   └── src/
│       ├── bayes.py
│       └── gradient_descent.py
```

## Day-by-Day Summary

### Day 1 - Probability
Introduction to probability, random events, and basic probability rules.

### Day 2 - Bayes' Theorem
Study of conditional probability and updating beliefs with new evidence.

### Day 3 - Probability Practice
More hands-on work with probability concepts and problem solving.

### Day 4 - Derivatives and Gradients
Understanding slope, change, and how derivatives help in optimization.

### Day 5 - Chain Rule
Learning how to compute derivatives of nested functions and complex expressions.

### Day 6 - Probability + Calculus for ML
Connecting probability, calculus, and machine learning thinking.

### Day 7 - Weekly Project and Review
Applying all concepts in a final summary activity and project challenge.

## Main Project
The major project for this week is the fraud detection exercise inside [week7-fraud_detection/README.md](week7-fraud_detection/README.md).

This project combines:
- Bayes' theorem for probability-based reasoning
- Gradient descent for optimization
- Data analysis for detecting suspicious transactions

## Key Concepts

### Bayes' Theorem
Used to calculate the probability of an event based on new evidence:

P(A|B) = P(B|A) × P(A) / P(B)

This is useful in classification and decision-making problems.

### Derivatives
Derivatives measure how a function changes as its input changes. They are central to optimization.

### Gradient Descent
Gradient descent is an optimization algorithm used to reduce model error by repeatedly updating parameters in the direction of the steepest decrease in loss.

## Tools Used
- Python
- NumPy
- Pandas
- Matplotlib
- Jupyter Notebook

## Expected Outcome
By the end of this week, you should be able to:
- reason about uncertainty using probability
- understand the math behind machine learning models
- apply Bayes' theorem in practical cases
- use gradient descent to optimize a model
- connect mathematical ideas to real data problems

## Suggested Next Step
Open the fraud detection project and practice implementing the concepts in code before moving to the next week.

---

Part of the AI Roadmap learning journey.
