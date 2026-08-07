from src.file_handler import read_expenses, add_expense, write_expenses


class ExpenseManager:

    def __init__(self):
        self.expenses = read_expenses()

    def add_new_expense(
        self,
        date,
        category,
        description,
        amount,
        payment_method
    ):
        expenses = read_expenses()

        new_id = len(expenses) + 1

        expense = {
            "id": str(new_id),
            "date": date,
            "category": category,
            "description": description,
            "amount": str(amount),
            "payment_method": payment_method
        }

        add_expense(expense)

        self.expenses = read_expenses()

        return expense

    def get_all_expenses(self):
        self.expenses = read_expenses()
        return self.expenses

    def search_expenses(self, keyword):
        expenses = read_expenses()
        keyword = keyword.lower()

        return [
            expense
            for expense in expenses
            if keyword in expense["date"].lower()
            or keyword in expense["category"].lower()
            or keyword in expense["description"].lower()
            or keyword in expense["payment_method"].lower()
        ]

    def update_expense(self, expense_id, updated_data):
        expenses = read_expenses()

        for expense in expenses:

            if expense["id"].strip() == expense_id.strip():

                for key, value in updated_data.items():
                    if value:
                        expense[key] = str(value)

                write_expenses(expenses)

                self.expenses = read_expenses()

                return True

        return False

    def delete_expense(self, expense_id):
        expenses = read_expenses()

        new_expenses = [
            expense
            for expense in expenses
            if expense["id"] != expense_id
        ]

        if len(new_expenses) == len(expenses):
            return False

        write_expenses(new_expenses)

        self.expenses = new_expenses

        return True

    def get_total_expense(self):
        expenses = read_expenses()

        return sum(
            float(expense["amount"])
            for expense in expenses
        )

    def get_category_summary(self):
        expenses = read_expenses()

        summary = {}

        for expense in expenses:
            category = expense["category"]
            amount = float(expense["amount"])

            summary[category] = (
                summary.get(category, 0) + amount
            )

        return summary

    def get_monthly_summary(self):
        expenses = read_expenses()

        summary = {}

        for expense in expenses:
            month = expense["date"][:7]
            amount = float(expense["amount"])

            summary[month] = (
                summary.get(month, 0) + amount
            )

        return summary
    