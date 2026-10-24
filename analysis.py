import math


def _amount(expense):
    """Return the amount of an expense, or raise ValueError."""
    try:
        value = expense["amount"]
    except (KeyError, TypeError):
        raise ValueError("Invalid expense amount")
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise ValueError("Amount must be numeric")
    if math.isnan(value) or math.isinf(value):
        raise ValueError("Amount must be a finite number")
    if value < 0:
        raise ValueError("Amount cannot be negative")
    return float(value)


def calculate_total(expenses):
    """Total spending across all expenses."""
    return sum(_amount(e) for e in expenses)


def total_by_category(expenses, category):
    """Total spending for one category (case-insensitive)."""
    if not isinstance(category, str) or not category.strip():
        raise ValueError("Category must be a non-empty string")
    wanted = category.strip().lower()
    return sum(
        _amount(e) for e in expenses
        if str(e.get("category", "")).strip().lower() == wanted
    )


def largest_expense(expenses):
    """Return the expense with the highest amount, or None if empty."""
    if not expenses:
        return None
    return max(expenses, key=_amount)