import pytest
from expenses import add_expense, edit_expense, delete_expense


def test_add_expense():
    expenses = []

    add_expense(expenses, 1, 50, "Food", "Lunch")

    assert len(expenses) == 1
    assert expenses[0]["amount"] == 50


def test_edit_expense():
    expenses = [
        {"id": 1, "amount": 50, "category": "Food", "description": "Lunch"}
    ]

    edit_expense(expenses, 1, 75, "Food", "Dinner")

    assert expenses[0]["amount"] == 75
    assert expenses[0]["description"] == "Dinner"

def test_add_expense_rejects_duplicate_id():
    expenses = [
        {
            "id": 1,
            "amount": 20.0,
            "category": "Food",
            "description": "Lunch"
        }
    ]

    with pytest.raises(ValueError):
        add_expense(expenses, 1, 30.0, "Transport", "Bus")

    assert len(expenses) == 1

def test_delete_nonexistent_expense():
    expenses = []

    with pytest.raises(ValueError):
        delete_expense(expenses, 999)