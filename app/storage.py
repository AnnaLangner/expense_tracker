import json
from datetime import date
from pathlib import Path
from .models import Expense

BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_DATA_FILE = BASE_DIR / "data" / "expenses.json"


def load_expenses(file_path: Path = DEFAULT_DATA_FILE) -> list[Expense]:
    if not file_path.exists():
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        raw_data = json.load(file)

    expenses = []
    for item in raw_data:
        expenses.append(
            Expense(
                date=date.fromisoformat(item["date"]),
                amount=float(item["amount"]),
                currency=item["currency"],
                category=item["category"],
                description=item["description"]
            )
        )

    return expenses


def save_expenses(
    expenses: list[Expense],
    file_path: Path = DEFAULT_DATA_FILE
) -> None:
    file_path.parent.mkdir(parents=True, exist_ok=True)

    data = []
    for e in expenses:
        data.append({
            "date": e.date.isoformat(),
            "amount": e.amount,
            "currency": e.currency,
            "category": e.category,
            "description": e.description
        })

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
