# User Guide – Expense Tracker

## 1. Introduction

Expense Tracker is a command-line Python application for managing daily expenses.

Users can add, view, search, update, and delete expenses.

---

## 2. How to Run

Open the project folder in VS Code.

Open the terminal and run:

```bash
python -m src.main
```

The following menu will appear:

```text
========================================
       EXPENSE TRACKER APPLICATION
========================================

1. Add Expense
2. View All Expenses
3. Search Expense
4. Update Expense
5. Delete Expense
6. Expense Summary
7. Monthly Report
8. Generate Reports
9. Exit
```

---

## 3. Add Expense

Select option **1**.

Enter:

```text
Date
Category
Description
Amount
Payment Method
```

Example:

```text
Enter date (YYYY-MM-DD): 2026-08-07
Enter category: Food
Enter description: Lunch
Enter amount: 250
Enter payment method: UPI
```

The expense will be saved with a unique ID.

---

## 4. View Expenses

Select option **2**.

The application displays all saved expenses.

Example:

```text
ID   Date        Category    Description    Amount
1    2026-08-01  Food        Breakfast      ₹120.00
2    2026-08-02  Travel      Bus Ticket     ₹80.00
```

---

## 5. Search Expense

Select option **3**.

Enter a keyword such as:

```text
Food
Travel
UPI
2026-08-01
```

The application displays matching expenses.

---

## 6. Update Expense

Select option **4**.

Enter the expense ID and provide the new information.

Example:

```text
Enter expense ID: 2
New amount: 100
```

The expense will be updated.

---

## 7. Delete Expense

Select option **5**.

Enter the expense ID.

Example:

```text
Enter expense ID: 2
```

The selected expense will be deleted.

---

## 8. Expense Summary

Select option **6**.

The application displays:

* Total expenses
* Highest expense
* Average expense
* Category-wise expenses

---

## 9. Monthly Report

Select option **7**.

The application displays expenses grouped by month.

---

## 10. Generate Reports

Select option **8**.

The application generates:

```text
outputs/
├── expense_report.txt
└── monthly_summary.txt
```

---

## 11. Exit

Select option **9** to close the application.

```text
Thank you for using Expense Tracker!
```

---

## 12. Testing

To run the tests, use:

```bash
python -m unittest discover tests
```

Expected result:

```text
......
----------------------------------------------------------------------
Ran 6 tests

OK
```

## 13. Conclusion

The application provides an easy way to record and manage personal expenses using Python.
