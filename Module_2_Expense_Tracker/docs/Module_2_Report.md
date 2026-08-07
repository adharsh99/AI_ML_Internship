# Module 2 Report – Expense Tracker

## 1. Project Title

**Expense Tracker**

## 2. Introduction

As part of Module 2 of the internship, an Expense Tracker application was developed using Python.

The project helps users manage their daily expenses and provides basic expense analysis.

## 3. Objective

The main objective is to develop a simple application that can:

* Store expenses
* View expenses
* Search expenses
* Update expenses
* Delete expenses
* Calculate summaries
* Generate reports

## 4. Technologies Used

* Python
* CSV
* Unittest
* VS Code
* Git
* GitHub

## 5. Project Structure

```text
Module_2_Expense_Tracker/
│
├── README.md
├── src/
│   ├── main.py
│   ├── expense_manager.py
│   ├── file_handler.py
│   ├── report_generator.py
│   ├── validator.py
│   └── utils.py
│
├── data/
├── config/
├── tests/
├── docs/
├── outputs/
└── .gitignore
```

## 6. Main Modules

### main.py

Contains the main menu and handles user interaction.

### expense_manager.py

Handles adding, viewing, searching, updating, and deleting expenses.

### file_handler.py

Handles CSV file operations.

### validator.py

Validates user input such as date, amount, category, and payment method.

### report_generator.py

Creates expense and monthly reports.

### utils.py

Contains common helper functions.

### settings.py

Contains project configuration values.

## 7. Main Features

### Add Expense

Users can enter the date, category, description, amount, and payment method.

### View Expenses

Displays all stored expenses.

### Search Expense

Allows users to search for expenses.

### Update Expense

Allows existing expense information to be modified.

### Delete Expense

Allows unwanted expenses to be removed.

### Expense Summary

Displays total, highest, average, and category-wise expenses.

### Monthly Report

Displays expenses according to the month.

## 8. Data Storage

Expense data is stored in:

```text
data/expenses.csv
```

Example:

```csv
id,date,category,description,amount,payment_method
1,2026-08-01,Food,Breakfast,120,UPI
2,2026-08-02,Travel,Bus Ticket,80,Cash
```

## 9. Testing

Unit testing was performed using Python's `unittest` module.

Command:

```bash
python -m unittest discover tests
```

Expected output:

```text
......
----------------------------------------------------------------------
Ran 6 tests

OK
```

## 10. Screenshots

The following screenshots are included in the project:

1. Project Structure
2. Add Expense
3. View Expenses
4. Search Expense
5. Expense Summary
6. CSV Data
7. Testing
8. GitHub Repository

Screenshots are stored in:

```text
docs/Screenshots/
```

## 11. Result

The Expense Tracker was successfully developed.

The application can store and manage expenses and generate useful summaries and reports.

## 12. Learning Outcomes

Through this project, I learned and practiced:

* Python programming
* Functions
* Modules
* File handling
* CSV handling
* Classes and objects
* Input validation
* Unit testing
* Git and GitHub
* Project documentation

## 13. Future Enhancements

The project can be improved by adding:

* GUI
* Database
* Expense charts
* Login system
* Excel/PDF reports
* Web application

## 14. Conclusion

The Expense Tracker project provided practical experience in Python application development. It helped in understanding how different Python concepts can be combined to create a useful real-world application.