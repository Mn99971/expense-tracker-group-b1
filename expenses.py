
# expenses.py
"""Expense management functions for the group expense tracker."""


def add_expense(expenses, expense_id, amount, category, description):
    """Add an expense and return the updated list."""
    if not isinstance(amount, (int, float)) or isinstance(amount, bool):
        raise ValueError("Amount must be numeric")
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if any(expense["id"] == expense_id for expense in expenses):
        raise ValueError("Expense ID already exists")

    expense = {
        "id": expense_id,
        "amount": amount,
        "category": category,
        "description": description,
    }
    expenses.append(expense)
    return expenses


def edit_expense(expenses, expense_id, amount, category, description):
    """Update an existing expense and return the updated list."""
    if not isinstance(amount, (int, float)) or isinstance(amount, bool):
        raise ValueError("Amount must be numeric")
    if amount <= 0:
        raise ValueError("Amount must be positive")

    for expense in expenses:
        if expense["id"] == expense_id:
            expense["amount"] = amount
            expense["category"] = category
            expense["description"] = description
            return expenses

    raise ValueError("Expense not found")


def delete_expense(expenses, expense_id):
    """Remove an expense by ID and return the updated list."""
    for index, expense in enumerate(expenses):
        if expense["id"] == expense_id:
            expenses.pop(index)
            return expenses

    raise ValueError("Expense not found")
