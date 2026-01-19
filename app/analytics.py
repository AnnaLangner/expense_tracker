import matplotlib
matplotlib.use("Agg")

import os
import matplotlib.pyplot as plt
from app.models import Expense
from app.reports import total_per_category


def plot_expenses_by_category(expenses: list[Expense], output_path: str, title: str = "Expenses by Category") -> None:
    totals = total_per_category(expenses)

    categories = list(totals.keys())
    amounts = list(totals.values())

    plt.figure(figsize=(8, 5))
    plt.bar(categories, amounts, color="skyblue")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.title(title)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    plt.close()
