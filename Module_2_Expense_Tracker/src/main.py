from src.expense_manager import ExpenseManager
from src.report_generator import (
    generate_expense_report,
    generate_monthly_summary
)

from src.validator import (
    validate_date,
    validate_amount,
    validate_category,
    validate_payment_method,
    validate_description
)

from config.settings import CATEGORIES, PAYMENT_METHODS
from src.utils import display_title, format_currency


manager = ExpenseManager()


def add_expense():
    display_title("ADD EXPENSE")

    date = input("Enter date (YYYY-MM-DD): ").strip()

    if not validate_date(date):
        print("Invalid date format.")
        return

    print("\nAvailable Categories:")

    for category in CATEGORIES:
        print("-", category)

    category = input("Enter category: ").strip().title()

    if not validate_category(category):
        print("Invalid category.")
        return

    description = input("Enter description: ").strip()

    if not validate_description(description):
        print("Description cannot be empty.")
        return

    amount = input("Enter amount: ").strip()

    if not validate_amount(amount):
        print("Invalid amount.")
        return

    print("\nPayment Methods:")

    for method in PAYMENT_METHODS:
        print("-", method)

    payment_method = input("Enter payment method: ").strip().title()

    if not validate_payment_method(payment_method):
        print("Invalid payment method.")
        return

    expense = manager.add_new_expense(
        date,
        category,
        description,
        amount,
        payment_method
    )

    print("\nExpense added successfully!")
    print("Expense ID:", expense["id"])


def view_expenses():
    display_title("ALL EXPENSES")

    expenses = manager.get_all_expenses()

    if not expenses:
        print("No expenses found.")
        return

    print(
        f"{'ID':<5}"
        f"{'Date':<15}"
        f"{'Category':<15}"
        f"{'Description':<20}"
        f"{'Amount':<15}"
        f"{'Payment':<15}"
    )

    print("-" * 85)

    for expense in expenses:

        print(
            f"{expense['id']:<5}"
            f"{expense['date']:<15}"
            f"{expense['category']:<15}"
            f"{expense['description']:<20}"
            f"{format_currency(expense['amount']):<15}"
            f"{expense['payment_method']:<15}"
        )


def search_expense():
    display_title("SEARCH EXPENSE")

    keyword = input(
        "Enter date/category/description/payment method: "
    ).strip()

    results = manager.search_expenses(keyword)

    if not results:
        print("No matching expenses found.")
        return

    for expense in results:

        print(
            f"\nID: {expense['id']}\n"
            f"Date: {expense['date']}\n"
            f"Category: {expense['category']}\n"
            f"Description: {expense['description']}\n"
            f"Amount: {format_currency(expense['amount'])}\n"
            f"Payment Method: {expense['payment_method']}"
        )


def update_expense():
    display_title("UPDATE EXPENSE")

    expense_id = input("Enter expense ID: ").strip()

    print("\nPress Enter to keep the existing value.")

    date = input("New date (YYYY-MM-DD): ").strip()

    if date and not validate_date(date):
        print("Invalid date.")
        return

    category = input("New category: ").strip().title()

    if category and not validate_category(category):
        print("Invalid category.")
        return

    description = input("New description: ").strip()

    amount = input("New amount: ").strip()

    if amount and not validate_amount(amount):
        print("Invalid amount.")
        return

    payment_method = input(
        "New payment method: "
    ).strip().title()

    if (
        payment_method
        and not validate_payment_method(payment_method)
    ):
        print("Invalid payment method.")
        return

    updated_data = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount,
        "payment_method": payment_method
    }

    success = manager.update_expense(
        expense_id,
        updated_data
    )

    if success:
        print("Expense updated successfully!")
    else:
        print("Expense ID not found.")


def delete_expense():
    display_title("DELETE EXPENSE")

    expense_id = input("Enter expense ID: ").strip()

    success = manager.delete_expense(expense_id)

    if success:
        print("Expense deleted successfully!")
    else:
        print("Expense ID not found.")


def expense_summary():
    display_title("EXPENSE SUMMARY")

    expenses = manager.get_all_expenses()

    if not expenses:
        print("No expenses available.")
        return

    total = manager.get_total_expense()

    amounts = [
        float(expense["amount"])
        for expense in expenses
    ]

    highest = max(amounts)
    average = sum(amounts) / len(amounts)

    print("Total Expenses :", format_currency(total))
    print("Highest Expense:", format_currency(highest))
    print("Average Expense:", format_currency(average))

    print("\nCATEGORY SUMMARY")
    print("-" * 40)

    category_summary = manager.get_category_summary()

    for category, amount in category_summary.items():
        print(
            f"{category:<20} "
            f"{format_currency(amount)}"
        )


def monthly_report():
    display_title("MONTHLY REPORT")

    summary = manager.get_monthly_summary()

    if not summary:
        print("No expenses available.")
        return

    for month, amount in sorted(summary.items()):

        print(
            f"{month:<15}"
            f"{format_currency(amount)}"
        )


def generate_reports():
    generate_expense_report()
    generate_monthly_summary()

    print("Reports generated successfully!")
    print("Check the outputs folder.")


def show_menu():

    while True:

        display_title("EXPENSE TRACKER APPLICATION")

        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search Expense")
        print("4. Update Expense")
        print("5. Delete Expense")
        print("6. Expense Summary")
        print("7. Monthly Report")
        print("8. Generate Reports")
        print("9. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            search_expense()

        elif choice == "4":
            update_expense()

        elif choice == "5":
            delete_expense()

        elif choice == "6":
            expense_summary()

        elif choice == "7":
            monthly_report()

        elif choice == "8":
            generate_reports()

        elif choice == "9":
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    show_menu()