
# expenses.py

"""Expense management functions for the group expense tracker."""

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("expenses.json")

def load_expenses():
    """Load expenses, handling missing, empty, or invalid JSON."""
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            content = file.read().strip()

        if not content:
            return []

        expenses = json.loads(content)
        if not isinstance(expenses, list):
            raise ValueError("Expense data must be a list")
        return expenses

    except json.JSONDecodeError as error:
        raise ValueError("Expense data file contains invalid JSON") from error


def save_expenses(expenses):
    """Save expenses to a local JSON file."""
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses, expense_id, amount, category, description):
    """Add an expense and return the updated list."""
    validate_amount(amount)

    expense = {
        "id": expense_id,
        "amount": amount,
        "category": category,
        "description": description,
    }
    if any(expense["id"] == expense_id for expense in expenses):
        raise ValueError("An expense with this ID already exists")
    expenses.append(expense)
    return expenses


def edit_expense(expenses, expense_id, amount, category, description):
    """Update an existing expense and return the updated list."""
    validate_amount(amount)

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

def validate_amount(amount):
    if isinstance(amount, bool) or not isinstance(amount, (int, float)):
        raise ValueError("Amount must be numeric")
    if amount <= 0:
        raise ValueError("Amount must be positive")