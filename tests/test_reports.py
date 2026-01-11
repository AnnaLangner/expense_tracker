from datetime import date
from app.models import Expense
from app.reports import total_expenditures, total_per_category


def sample_expenses():
    return [
        Expense(date(2026, 1, 3), 150, "PLN", "Food", "Dinner"),
        Expense(date(2026, 1, 5), 20, "PLN", "Transport", "Bus"),
        Expense(date(2026, 1, 8), 200, "PLN", "Food", "Lunch"),
        Expense(date(2026, 1, 10), 50, "PLN", "Food", "Breakfast"),
    ]


def test_total_expenditures():
    result = total_expenditures(sample_expenses())
    assert result == 420


def test_total_per_category():
    result = total_per_category(sample_expenses())

    assert result["Food"] == 400
    assert result["Transport"] == 20
