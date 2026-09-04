# 📱 Dubai Mobile Market — Exploratory Data Analysis

## Project Overview

This project performs an Exploratory Data Analysis (EDA) of a mobile phone dataset.

The goal is to investigate mobile phone prices, brands, RAM, storage capacity, and ratings, and identify patterns that could help a mobile retailer better understand product positioning.

> **Note:** The dataset used in this project is a small educational dataset created for demonstrating the EDA workflow. It should not be interpreted as a representative sample of the entire Dubai mobile market.

## 🎯 Business Problem

A mobile retailer wants to understand:

* How mobile phone prices are distributed
* Which brands have higher or lower average prices
* Whether RAM is associated with price
* Whether storage is associated with price
* Whether unusual price values exist
* Which numerical features have the strongest relationship with price

## 👤 Target User

**Mobile store owners, retailers, and distributors** who want to explore product pricing and specifications.

## 🛠️ Technologies

* Python
* Pandas
* Matplotlib
* Seaborn
* Jupyter Notebook

## 📊 Dataset Features

| Feature      | Description            |
| ------------ | ---------------------- |
| `brand`      | Mobile phone brand     |
| `model`      | Mobile phone model     |
| `price`      | Price in AED           |
| `ram_gb`     | RAM capacity in GB     |
| `storage_gb` | Storage capacity in GB |
| `rating`     | Product rating         |

## 🔍 Analysis Performed

### 1. Dataset Overview

* Dataset shape
* Data types
* Descriptive statistics
* Missing-value analysis
* Duplicate-value analysis

### 2. Price Analysis

* Mean price
* Median price
* Minimum price
* Maximum price
* Price distribution

### 3. Brand Analysis

* Number of products by brand
* Average price by brand
* Brand-level price comparison

### 4. RAM & Storage Analysis

* RAM distribution
* RAM vs. price
* Storage vs. price

### 5. Outlier Analysis

* Price box plots
* Interquartile range (IQR)
* Potential price outliers

### 6. Correlation Analysis

A correlation matrix and heatmap were used to investigate relationships between numerical variables.

## 📈 Visualizations

The project includes:

* Histograms
* Scatter plots
* Box plots
* Bar charts
* Correlation heatmap

## 💡 Key Findings

* Higher-priced devices are concentrated among several premium brands in this sample.
* Higher RAM generally appears alongside higher prices.
* Larger storage capacities generally appear at higher price points.
* Several products may appear as potential price outliers and should be investigated before removal.
* Correlation analysis provides a quantitative way to compare relationships between numerical features.

## ⚠️ Limitations

This dataset is intentionally small and was created for learning and portfolio practice.

Therefore:

* It does not represent the entire Dubai mobile market.
* The sample is not statistically representative.
* Correlation does not prove causation.
* Business decisions should use a larger real-world dataset.

## 🚀 How to Run

Clone the repository and install the required packages:

```bash
pip install -r requirements.txt
```

Then start Jupyter:

```bash
jupyter notebook
```

Open:

```text
notebooks/mobile_market_eda.ipynb
```

## 📂 Project Structure

```text
dubai-mobile-market-eda/
│
├── data/
│   └── mobile_data.csv
│
├── notebooks/
│   └── mobile_market_eda.ipynb
│
├── images/
│   └── average_price_by_brand.png
│
├── README.md
│
└── requirements.txt
```

## 👨‍💻 Skills Demonstrated

This project demonstrates practical experience with:

* Python data analysis
* Pandas
* Data cleaning
* Descriptive statistics
* Exploratory Data Analysis
* Data visualization
* Matplotlib
* Seaborn
* Correlation analysis
* Outlier detection
* Business-oriented data interpretation
* GitHub project organization
