from datetime import date
from app.models import Expense
from app.logic import filter_expenses


def sample_expenses():
    return [
        Expense(date(2026, 1, 3), 150, "PLN", "Food", "Dinner"),
        Expense(date(2026, 1, 5), 20, "EUR", "Transport", "Bus"),
        Expense(date(2026, 1, 8), 200, "PLN", "Food", "Lunch"),
        Expense(date(2026, 1, 10), 50, "EUR", "Food", "Breakfast"),
    ]


def test_filter_by_category():
    result = filter_expenses(sample_expenses(), category="Food")
    assert len(result) == 3


def test_filter_by_currency():
    result = filter_expenses(sample_expenses(), currency="PLN")
    assert len(result) == 2


def test_filter_by_date_range():
    result = filter_expenses(
        sample_expenses(),
        date_from=date(2026, 1, 2),
        date_to=date(2026, 1, 6)
    )
    assert len(result) == 2


def test_filter_combined():
    result = filter_expenses(
        sample_expenses(),
        category="Food",
        currency="EUR"
    )
    assert len(result) == 1
