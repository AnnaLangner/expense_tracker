from __future__ import annotations
from datetime import date
from pathlib import Path
from .models import Expense
from .storage import load_expenses, save_expenses


def add_expense(
    expense_date: date,
    amount: float,
    currency: str,
    category: str,
    description: str,
    file_path: Path | None = None
) -> Expense:

    if amount <= 0:
        raise ValueError("Amount must be greater than zero")

    if not currency:
        raise ValueError("Currency is required")

    if not category:
        raise ValueError("Category is required")

    expenses = load_expenses(file_path) if file_path else load_expenses()

    expense = Expense(
        date=expense_date,
        amount=amount,
        currency=currency,
        category=category,
        description=description
    )

    expenses.append(expense)

    if file_path:
        save_expenses(expenses, file_path)
    else:
        save_expenses(expenses)

    return expense


def get_all_expenses(file_path: Path | None = None) -> list[Expense]:
    return load_expenses(file_path) if file_path else load_expenses()
