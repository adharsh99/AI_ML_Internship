import unittest

from src.expense_manager import ExpenseManager
from src.validator import (
    validate_amount,
    validate_date,
    validate_description
)


class TestExpenseTracker(unittest.TestCase):

    def setUp(self):
        self.manager = ExpenseManager()

    def test_valid_amount(self):
        self.assertTrue(
            validate_amount("500")
        )

    def test_invalid_amount(self):
        self.assertFalse(
            validate_amount("-100")
        )

    def test_valid_date(self):
        self.assertTrue(
            validate_date("2026-08-07")
        )

    def test_invalid_date(self):
        self.assertFalse(
            validate_date("07-08-2026")
        )

    def test_valid_description(self):
        self.assertTrue(
            validate_description("Lunch")
        )

    def test_empty_description(self):
        self.assertFalse(
            validate_description("")
        )


if __name__ == "__main__":
    unittest.main()
    