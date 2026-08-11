import csv
import os

from config.settings import DATA_FILE


def read_expenses():
    """
    Read expenses from the CSV file.
    Supports the existing CSV format without ID.
    """

    if not os.path.exists(DATA_FILE):
        return []

    with open(
        DATA_FILE,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)
        expenses = []

        for index, row in enumerate(reader, start=1):

            expense = {
                "id": str(index),
                "date": row.get("Date", row.get("date", "")),
                "category": row.get(
                    "Category",
                    row.get("category", "")
                ),
                "description": row.get(
                    "Description",
                    row.get("description", "")
                ),
                "amount": row.get(
                    "Amount",
                    row.get("amount", "0")
                ),
                "payment_method": row.get(
                    "Payment_Method",
                    row.get("payment_method", "")
                )
            }

            expenses.append(expense)

        return expenses


def add_expense(expense):
    """
    Add a new expense to the CSV file.
    """

    expenses = read_expenses()

    # Generate the next ID
    expense["id"] = str(len(expenses) + 1)

    expenses.append(expense)

    write_expenses(expenses)


def write_expenses(expenses):
    """
    Write all expenses to the CSV file.
    """

    os.makedirs(
        os.path.dirname(DATA_FILE),
        exist_ok=True
    )

    fieldnames = [
        "id",
        "date",
        "category",
        "description",
        "amount",
        "payment_method"
    ]

    with open(
        DATA_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        writer.writerows(expenses)
        