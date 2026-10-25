import pytest
from analysis import calculate_total, total_by_category, largest_expense

EXPENSES = [
    {"id": 1, "amount": 50.0, "category": "Food", "description": "Lunch"},
    {"id": 2, "amount": 20.0, "category": "Transport", "description": "Bus"},
    {"id": 3, "amount": 30.0, "category": "Food", "description": "Dinner"},
]


def test_calculate_total_normal():
    assert calculate_total(EXPENSES) == 100.0


def test_total_by_category_normal():
    assert total_by_category(EXPENSES, "Food") == 80.0


def test_largest_expense_normal():
    assert largest_expense(EXPENSES)["id"] == 1


def test_empty_list_edge_case():
    assert calculate_total([]) == 0
    assert largest_expense([]) is None


def test_invalid_amount_raises_value_error():
    bad = [{"id": 1, "amount": "abc", "category": "Food", "description": "x"}]
    with pytest.raises(ValueError):
        calculate_total(bad)

def test_numeric_string_amount_is_rejected():
    bad = [{"id": 1, "amount": "50", "category": "Food", "description": "x"}]
    with pytest.raises(ValueError):
        calculate_total(bad)


def test_nan_amount_is_rejected():
    bad = [{"id": 1, "amount": float("nan"), "category": "Food", "description": "x"}]
    with pytest.raises(ValueError):
        calculate_total(bad)