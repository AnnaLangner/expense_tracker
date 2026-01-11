import pytest
from datetime import date
from app.logic import add_expense, get_all_expenses


def test_add_expense(tmp_path):
    test_file = tmp_path / "expenses.json"

    expense = add_expense(
        expense_date=date(2026, 1, 1),
        amount=50.0,
        currency="PLN",
        category="Food",
        description="Lunch",
        file_path=test_file
    )

    expenses = get_all_expenses(file_path=test_file)

    assert len(expenses) == 1
    assert expenses[0] == expense


def test_add_expense_invalid_amount(tmp_path):
    with pytest.raises(ValueError):
        add_expense(
            expense_date=date.today(),
            amount=0,
            currency="PLN",
            category="Food",
            description="Test",
            file_path=tmp_path / "expenses.json"
        )
