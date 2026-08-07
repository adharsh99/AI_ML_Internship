import os


# Main project directory
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


# Data folder
DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)


# Output folder
OUTPUT_DIR = os.path.join(
    BASE_DIR,
    "outputs"
)


# Expense CSV file
DATA_FILE = os.path.join(
    DATA_DIR,
    "expenses.csv"
)


# Expense report file
EXPENSE_REPORT_FILE = os.path.join(
    OUTPUT_DIR,
    "expense_report.txt"
)


# Monthly summary file
MONTHLY_SUMMARY_FILE = os.path.join(
    OUTPUT_DIR,
    "monthly_summary.txt"
)


# Expense categories
CATEGORIES = [
    "Food",
    "Travel",
    "Shopping",
    "Bills",
    "Education",
    "Entertainment",
    "Health",
    "Other"
]


# Payment methods

PAYMENT_METHODS = [
    "Cash",
    "UPI",
    "Card",
    "Net Banking"
]