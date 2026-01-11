from app.logic import get_all_expenses, filter_expenses
from app.reports import total_expenditures, total_per_category


def main():
    expenses = get_all_expenses()

    food_expenses = filter_expenses(expenses, category="Food")

    print("Total Food expenses:", total_expenditures(food_expenses))
    print("Total per category:", total_per_category(expenses))


if __name__ == "__main__":
    main()
