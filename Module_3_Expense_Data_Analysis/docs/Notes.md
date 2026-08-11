# Module 3 – Data Analysis & Visualization Notes

## 1. Introduction

Module 3 focuses on Data Analysis and Visualization using Python.

In this module, we learned how to work with datasets using Pandas and
NumPy. We also learned how to clean, analyze, and visualize data using
Matplotlib.

The expense dataset created in Module 2 was used for this analysis.

---

## 2. Objectives

The main objectives of Module 3 are:

- Learn how to work with datasets.
- Learn Pandas and NumPy.
- Load and explore a dataset.
- Perform basic data cleaning.
- Perform simple data analysis.
- Calculate important statistics.
- Create charts using Matplotlib.
- Understand data patterns and insights.

---

## 3. Tools Used

### Python

Python is the main programming language used for data analysis.

### Pandas

Pandas is a Python library used for:

- Reading datasets.
- Cleaning data.
- Manipulating data.
- Analyzing data.
- Working with tables and DataFrames.

### NumPy

NumPy is used for numerical operations and calculations.

### Matplotlib

Matplotlib is used to create graphs and charts.

### Google Colab

Google Colab was used to write and execute the Python code.

---

## 4. Dataset

The dataset used in this module is:

expenses.csv

The dataset was created in Module 2 and used in Module 3 for analysis.

The main columns are:

- id
- date
- category
- description
- amount
- payment_method

---

## 5. Loading the Dataset

The Pandas library was imported first.

Example:

import pandas as pd

The CSV file was then loaded using:

df = pd.read_csv("/expenses.csv")

The data was stored in a variable called df.

---

## 6. Understanding the Dataset

The dataset was explored using different Pandas functions.

### Shape

df.shape

This shows the number of rows and columns.

### Column Names

df.columns

This displays all column names.

### First Five Records

df.head()

This displays the first five records.

---

## 7. Data Information

The info() function was used to understand the structure of the dataset.

Example:

df.info()

It provides information about:

- Column names.
- Number of records.
- Data types.
- Non-null values.

---

## 8. Missing Values

Missing values were checked using:

df.isnull().sum()

This helps identify empty or missing data in each column.

Checking missing values is important before performing data analysis.

---

## 9. Basic Statistics

The describe() function was used to generate basic statistical information.

Example:

df.describe()

It provides values such as:

- Count
- Mean
- Standard deviation
- Minimum
- Maximum

This is useful for understanding numerical data such as expense amounts.

---

## 10. Total Expense

The total amount spent was calculated using the sum() function.

Example:

total_expense = df["amount"].sum()

print("Total Expense:", total_expense)

This gives the total amount of all expenses in the dataset.

---

## 11. Average Expense

The average expense was calculated using the mean() function.

Example:

average_expense = df["amount"].mean()

print("Average Expense:", average_expense)

This shows the average amount spent per transaction.

---

## 12. Highest Expense

The highest expense was identified using idxmax().

Example:

highest_expense = df.loc[df["amount"].idxmax()]

print("Highest Expense:")
display(highest_expense)

This helps identify the transaction with the highest amount.

---

## 13. Lowest Expense

The lowest expense was identified using idxmin().

Example:

lowest_expense = df.loc[df["amount"].idxmin()]

print("Lowest Expense:")
display(lowest_expense)

This helps identify the transaction with the lowest amount.

---

## 14. Category-wise Analysis

Expenses were grouped according to their categories.

Example:

category_expense = df.groupby("category")["amount"].sum()

print(category_expense)

This helps identify how much money was spent on each category.

Examples of categories include:

- Bills
- Education
- Food
- Travel

---

## 15. Category-wise Visualization

A bar chart was created to visualize category-wise expenses.

Example:

category_expense.plot(kind="bar")

plt.title("Expenses by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.show()

The bar chart makes it easier to compare different expense categories.

---

## 16. Payment Method Analysis

Expenses were grouped according to payment methods.

Example:

payment_expense = df.groupby("payment_method")["amount"].sum()

print(payment_expense)

This shows how much money was spent using each payment method.

Examples include:

- UPI
- Cash
- Card

---

## 17. Payment Method Visualization

A pie chart was created to visualize expenses by payment method.

Example:

payment_expense.plot(kind="pie", autopct="%1.1f%%")

plt.title("Expenses by Payment Method")
plt.ylabel("")
plt.show()

The pie chart shows the percentage distribution of expenses.

---

## 18. Date Conversion

The date column was converted into a proper datetime format.

Example:

df["date"] = pd.to_datetime(df["date"])

This makes it easier to perform time-based analysis.

---

## 19. Monthly Expense Analysis

The month was extracted from the date column.

Example:

df["month"] = df["date"].dt.month

Monthly expenses were then calculated:

monthly_expense = df.groupby("month")["amount"].sum()

print(monthly_expense)

This helps understand spending patterns across different months.

---

## 20. Monthly Expense Visualization

A line chart was created to visualize monthly expenses.

Example:

monthly_expense.plot(kind="line", marker="o")

plt.title("Monthly Expenses")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.show()

The line chart helps identify changes in spending over time.

---

## 21. Key Findings

The analysis helped identify:

- Total expenses.
- Average expense.
- Highest expense.
- Lowest expense.
- Highest spending category.
- Payment methods used.
- Monthly spending patterns.

These results help understand where money is being spent.

---

## 22. Data Visualization

Three main visualizations were created:

1. Expenses by Category – Bar Chart
2. Expenses by Payment Method – Pie Chart
3. Monthly Expenses – Line Chart

These visualizations make the analysis easier to understand.

---

## 23. Learning Outcomes

After completing Module 3, I learned:

- How to load CSV files using Pandas.
- How to work with DataFrames.
- How to inspect datasets.
- How to check missing values.
- How to perform basic statistical analysis.
- How to group and summarize data.
- How to work with dates.
- How to create bar charts.
- How to create pie charts.
- How to create line charts.
- How to understand data patterns.

---

## 24. Conclusion

Module 3 provided practical experience in Data Analysis and Visualization.

The expense dataset was loaded and explored using Pandas. Basic data
cleaning and statistical analysis were performed. Expense data was
analyzed based on categories, payment methods, and months.

Matplotlib was used to create different visualizations such as bar,
pie, and line charts.

This module helped develop a basic understanding of how Python can be
used to analyze real-world datasets and present useful insights through
visualizations.