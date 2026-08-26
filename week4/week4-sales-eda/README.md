# Sales EDA Project

This project explores a sample sales dataset and performs exploratory data analysis (EDA) to clean inconsistent values, identify missing data, and summarize business insights by region and product.

## Project Goal

The main goal is to analyze sales performance and answer questions such as:

- Which region has the highest total sales?
- Which product generates the most revenue?
- What data-quality issues are present in the dataset?
- How do sales totals change across different products and regions?

## Folder Structure

- `data/` - contains the raw dataset used for analysis
- `notebooks/` - contains the Jupyter notebook with the EDA workflow
- `requirements.txt` - project dependency list
- `README.md` - project overview and instructions

## Dataset

The dataset is stored in `data/sales_data.csv` and includes information such as:

- `order_id`
- `customer_id`
- `region`
- `product`
- `sales`
- `quantity`

During the analysis, the data is cleaned by:

- converting sales values to numeric format
- fixing inconsistent region and product labels
- handling missing values
- removing or flagging invalid values
- checking duplicate records

## Tools Used

This project is built with Python and commonly uses:

- pandas
- NumPy
- Jupyter Notebook

## Setup

1. Open the project folder.
2. Create a virtual environment if needed.
3. Install the required packages:

```bash
pip install pandas numpy jupyter
```

## Running the Notebook

Open the notebook in the `notebooks/` folder and run the cells in order:

- `sales_eda.ipynb`

The notebook includes:

- data loading
- initial inspection
- null and duplicate checks
- value cleaning
- descriptive statistics
- grouping and aggregation
- pivot table analysis
- summary insights

## Key Insights

The EDA workflow identifies:

- total sales by region
- total sales by product
- top-performing region and product
- missing values and data inconsistencies
- meaningful summary metrics for decision-making

## Example Analysis

The notebook calculates metrics like:

```python
sales_by_region = df.groupby("region")["sales"].sum().sort_values(ascending=False)
sales_by_product = df.groupby("product")["sales"].sum().sort_values(ascending=False)
```

## Notes

This project is designed as a beginner-friendly EDA example to practice real-world data cleaning and reporting in Python.
