# Fraud Detection Project

A machine learning project combining **Bayes' Theorem** and **Gradient Descent** to detect fraudulent transactions in financial data.

## 📋 Project Overview

This project demonstrates practical applications of Week 7 concepts:
- **Bayesian Statistics**: Using Bayes' theorem to calculate probability of fraud given evidence
- **Calculus & Gradient Descent**: Optimizing model parameters through iterative weight updates
- **Data Analysis**: Exploring transaction patterns and identifying fraud indicators

## 🏗️ Project Structure

```
week7-fraud_detection/
├── README.md                  # Project documentation
├── reqquirements.txt          # Python dependencies
├── data/
│   └── transactions.csv       # Transaction dataset for analysis
├── notebooks/
│   └── fraud_detection.ipynb  # Jupyter notebook with exploratory analysis
└── src/
    ├── bayes.py               # Bayes' theorem implementation
    └── gradient_descent.py    # Gradient descent optimization functions
```

## 🔑 Key Concepts

### Bayes' Theorem
Calculates the probability of fraud given observed evidence (e.g., new device, unusual amount):

$$P(Fraud|Evidence) = \frac{P(Evidence|Fraud) \times P(Fraud)}{P(Evidence)}$$

Where:
- **Prior**: P(Fraud) - Initial probability of fraud
- **Likelihood**: P(Evidence|Fraud) - Probability of observing evidence if fraud occurs
- **Evidence**: P(Evidence) - Overall probability of observing the evidence
- **Posterior**: P(Fraud|Evidence) - Updated probability after seeing evidence

### Gradient Descent
Optimizes model parameters by iteratively reducing loss:

$$\theta_{new} = \theta_{old} - \alpha \times \nabla L(\theta)$$

Where:
- **Learning rate (α)**: Controls step size in optimization
- **Gradient**: Direction of steepest loss increase
- **Loss**: Difference between prediction and actual value

## 📂 File Descriptions

### `src/bayes.py`
Implements Bayes' theorem to compute posterior probability:
- `bayes_theorem(prior, likelihood, evidence)` - Returns posterior probability

### `src/gradient_descent.py`
Core gradient descent functions:
- `calculate_prediction()` - Compute model output
- `calculate_loss()` - Squared error loss
- `calculate_gradient()` - Compute loss gradient
- `update_weight()` - Update parameters using gradient

### `data/transactions.csv`
Transaction dataset containing features like:
- Transaction amount
- User location/device
- Time of transaction
- Fraud label (1 = fraud, 0 = legitimate)

### `notebooks/fraud_detection.ipynb`
Jupyter notebook with:
- Data loading and exploration
- Bayesian fraud probability calculations
- Gradient descent model training and visualization

## 🚀 Getting Started

### Installation
```bash
# Install required dependencies
pip install -r reqquirements.txt
```

### Running the Analysis
```bash
# Run Bayes theorem analysis
python src/bayes.py

# Run gradient descent optimization
python src/gradient_descent.py

# Open Jupyter notebook for interactive analysis
jupyter notebook notebooks/fraud_detection.ipynb
```

## 📊 Example Usage

```python
from src.bayes import bayes_therom

# Calculate fraud probability
prior = 0.02          # 2% fraud rate
likelihood = 0.85     # 85% chance of new device if fraud
evidence = 0.10       # 10% of transactions use new device

posterior = bayes_therom(prior, likelihood, evidence)
print(f"Probability of fraud given new device: {posterior:.2%}")
```

## 🎯 Learning Objectives

- ✅ Apply Bayes' theorem to real-world classification problem
- ✅ Understand gradient descent optimization
- ✅ Implement and visualize fraud detection model
- ✅ Analyze financial transaction patterns
- ✅ Calculate probabilities and derivatives

## 📚 References

- **Bayes' Theorem**: Fundamental to probabilistic reasoning and classification
- **Gradient Descent**: Core optimization algorithm in machine learning
- **Calculus**: Computing derivatives for loss function minimization

## 🔧 Technologies

- Python 3.x
- Jupyter Notebook
- Pandas (data manipulation)
- NumPy (numerical computing)
- Matplotlib/Seaborn (visualization)

---

**Part of Week 7: Probability, Calculus, and Optimization concepts in the AI Roadmap**
