from datetime import datetime

from config.settings import CATEGORIES, PAYMENT_METHODS


def validate_date(date):
    """
    Validate date in YYYY-MM-DD format.
    """
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True

    except ValueError:
        return False


def validate_amount(amount):
    """
    Validate that amount is a positive number.
    """
    try:
        return float(amount) > 0

    except (ValueError, TypeError):
        return False


def validate_category(category):
    """
    Validate category without considering uppercase/lowercase.
    """
    category = category.strip().lower()

    return category in [
        item.lower()
        for item in CATEGORIES
    ]


def validate_payment_method(payment_method):
    """
    Validate payment method without considering uppercase/lowercase.
    """
    payment_method = payment_method.strip().lower()

    return payment_method in [
        item.lower()
        for item in PAYMENT_METHODS
    ]


def validate_description(description):
    """
    Validate that description is not empty.
    """
    return bool(description.strip())