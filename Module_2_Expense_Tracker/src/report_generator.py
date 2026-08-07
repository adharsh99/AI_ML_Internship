from src.file_handler import read_expenses
from config.settings import EXPENSE_REPORT_FILE, MONTHLY_SUMMARY_FILE
from src.utils import format_currency


def generate_expense_report():
    expenses = read_expenses()

    with open(
        EXPENSE_REPORT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        file.write("EXPENSE REPORT\n")
        file.write("=" * 70 + "\n\n")

        if not expenses:
            file.write("No expenses available.\n")
            return

        total = 0

        for expense in expenses:

            amount = float(expense["amount"])
            total += amount

            file.write(
                f"ID: {expense['id']}\n"
                f"Date: {expense['date']}\n"
                f"Category: {expense['category']}\n"
                f"Description: {expense['description']}\n"
                f"Amount: {format_currency(amount)}\n"
                f"Payment Method: {expense['payment_method']}\n"
            )

            file.write("-" * 70 + "\n")

        file.write(
            f"\nTOTAL EXPENSE: {format_currency(total)}\n"
        )


def generate_monthly_summary():
    expenses = read_expenses()

    summary = {}

    for expense in expenses:

        month = expense["date"][:7]
        amount = float(expense["amount"])

        summary[month] = summary.get(month, 0) + amount

    with open(
        MONTHLY_SUMMARY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        file.write("MONTHLY EXPENSE SUMMARY\n")
        file.write("=" * 50 + "\n\n")

        if not summary:
            file.write("No expenses available.\n")
            return

        for month, amount in sorted(summary.items()):
            file.write(
                f"{month} : {format_currency(amount)}\n"
            )