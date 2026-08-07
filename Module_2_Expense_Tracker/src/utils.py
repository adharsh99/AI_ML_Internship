def print_line(length=70):
    print("=" * length)


def display_title(title):
    print_line()
    print(title.center(70))
    print_line()


def format_currency(amount):
    return f"₹{float(amount):,.2f}"


def get_next_id(expenses):
    if not expenses:
        return 1

    ids = []

    for expense in expenses:
        try:
            ids.append(int(expense["id"]))
        except (ValueError, KeyError):
            continue

    return max(ids, default=0) + 1