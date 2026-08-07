import csv
import os

from config.settings import DATA_FILE


def read_expenses():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def add_expense(expense):
    expenses = read_expenses()
    expenses.append(expense)
    write_expenses(expenses)


def write_expenses(expenses):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    fieldnames = [
        "id",
        "date",
        "category",
        "description",
        "amount",
        "payment_method"
    ]

    with open(DATA_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(expenses)
        