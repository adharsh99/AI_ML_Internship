from datetime import datetime
from config.settings import DATE_FORMAT, CATEGORIES, PAYMENT_METHODS


def validate_date(date):
    try:
        datetime.strptime(date, DATE_FORMAT)
        return True
    except ValueError:
        return False


def validate_amount(amount):
    try:
        amount = float(amount)
        return amount > 0
    except ValueError:
        return False


def validate_category(category):
    return category.strip().title() in CATEGORIES


def validate_payment_method(method):
    return method.strip().title() in PAYMENT_METHODS


def validate_description(description):
    return bool(description.strip())