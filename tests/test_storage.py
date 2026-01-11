from datetime import date
from app.models import Expense
from app.storage import save_expenses, load_expenses


def test_save_and_load_expenses(tmp_path):
    test_file = tmp_path / "expenses_test.json"

    expense = Expense(
        date=date(2026, 1, 1),
        amount=200.0,
        currency="PLN",
        category="Test",
        description="Test expense"
    )

    save_expenses([expense], file_path=test_file)
    loaded = load_expenses(file_path=test_file)

    assert len(loaded) == 1
    assert loaded[0].amount == 200.0
    assert loaded[0].category == "Test"
