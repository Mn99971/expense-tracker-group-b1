def set_budget(amount):
    if isinstance(amount, bool) or not isinstance(amount, (int, float)):
        raise ValueError("Budget must be a number")
    if amount <= 0:
        raise ValueError("Budget must be a positive number")
    return amount


def remaining_budget(budget, expenses):
    total = sum(e["amount"] for e in expenses)
    return budget - total


def is_over_budget(budget, expenses):
    total = sum(e["amount"] for e in expenses)
    return total > budget