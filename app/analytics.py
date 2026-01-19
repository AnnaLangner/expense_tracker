import matplotlib.pyplot as plt
from app.reports import total_per_category
from app.models import Expense


def plot_expenses_by_category(expenses: list[Expense], title: str = "Expenses by Category") -> None:
    totals = total_per_category(expenses)

    categories = list(totals.keys())
    amounts = list(totals.values())

    plt.figure(figsize=(8, 5))
    plt.bar(categories, amounts, color='skyblue')
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.title(title)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
