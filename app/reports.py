from collections import defaultdict
from app.models import Expense


def total_expenditures(expenses: list[Expense]) -> float:
    return sum(e.amount for e in expenses)


def total_per_category(expenses: list[Expense]) -> dict[str, float]:
    totals = defaultdict(float)

    for e in expenses:
        totals[e.category] += e.amount

    return dict(totals)
