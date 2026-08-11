# Module 3 – Data Analysis & Visualization

## Overview

Module 3 focuses on learning how to work with datasets using Python.
In this module, Pandas and NumPy are used for data analysis and Matplotlib
is used for creating visualizations.

## Objectives

- Learn how to work with datasets using Pandas and NumPy.
- Load and explore a dataset.
- Perform basic data cleaning.
- Perform simple data analysis.
- Create visualizations using Matplotlib.
- Understand spending patterns from expense data.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Google Colab

## Dataset

For this module, the expenses.csv dataset created in Module 2
was used for analysis.

The dataset contains the following columns:

- id – Unique expense ID
- date – Date of the expense
- category – Expense category
- description – Description of the expense
- amount – Expense amount
- payment_method – Method used for payment

## Data Analysis

The following operations were performed:

1. Loaded the expense dataset using Pandas.
2. Explored the dataset.
3. Checked rows and columns.
4. Checked column names.
5. Checked data types using info().
6. Checked for missing values.
7. Generated basic statistical information.
8. Calculated total expenses.
9. Calculated average expenses.
10. Identified the highest expense.
11. Identified the lowest expense.
12. Performed category-wise expense analysis.
13. Performed payment-method analysis.
14. Converted the date column into a proper date format.
15. Performed monthly expense analysis.

## Data Cleaning

Basic data cleaning and preparation were performed to make the
dataset suitable for analysis.

The date column was converted into a proper datetime format using Pandas.

df["date"] = pd.to_datetime(df["date"])

Missing values were also checked using:

df.isnull().sum()

## Data Visualizations

Matplotlib was used to create different charts for understanding
the expense data.

### 1. Expenses by Category

A bar chart was created to compare expenses across different categories.

### 2. Expenses by Payment Method

A pie chart was created to understand the distribution of expenses
based on payment methods.

### 3. Monthly Expenses

A line chart was created to understand expense patterns across months.

## Key Analysis

The analysis helps to identify:

- Total amount spent.
- Average expense.
- Highest individual expense.
- Lowest individual expense.
- Category with the highest spending.
- Most frequently used payment method.
- Monthly spending patterns.

## Project Structure

Module_3_Data_Analysis/
│
├── README.md
├── Module_3_Data_Analysis.ipynb
│
├── docs/
│   └── Module_3_Notes.md
│
└── visualizations/
    ├── category_expenses.png
    ├── payment_methods.png
    └── monthly_expenses.png

## Tools and Libraries

### Pandas

Used for loading, cleaning, manipulating, and analyzing the dataset.

### NumPy

Used for numerical operations and data analysis.

### Matplotlib

Used to create charts and visualize the data.

### Google Colab

Used to write and execute the Python data analysis notebook.

## Conclusion

Module 3 provided practical experience in Data Analysis and
Visualization using Python.

The expense dataset was explored, cleaned, and analyzed using
Pandas and NumPy. Different visualizations were created using
Matplotlib to understand category-wise, payment-method, and
monthly spending patterns.

This module helped develop a basic understanding of how Python
can be used to analyze real-world datasets and present insights
through visualizations.

## Submission

The completed data analysis notebook is available in:

Data_Analysis.ipynb

The notebook was created and executed using Google Colab.