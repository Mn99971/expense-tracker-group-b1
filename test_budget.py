import pytest
from budget import set_budget, remaining_budget, is_over_budget


def test_set_budget_valid():
    assert set_budget(100) == 100


def test_set_budget_negative_raises():
    with pytest.raises(ValueError):
        set_budget(-5)


def test_remaining_budget():
    expenses = [{"amount": 30}, {"amount": 20}]
    assert remaining_budget(100, expenses) == 50


def test_is_over_budget():
    expenses = [{"amount": 80}]
    assert is_over_budget(50, expenses) is True
    assert is_over_budget(100, expenses) is False