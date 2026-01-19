import os
from datetime import date
from app.logic import add_expense, get_all_expenses
from app.analytics import plot_expenses_by_category
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        amount = float(request.form["amount"])
        category = request.form["category"]
        currency = request.form["currency"]
        description = request.form["description"]

        add_expense(
            expense_date=date.today(),
            amount=amount,
            currency=currency,
            category=category,
            description=description
        )

        return redirect(url_for("expenses"))

    return render_template("add.html")


@app.route("/expenses")
def expenses():
    expenses = get_all_expenses()
    return render_template("expenses.html", expenses=expenses)


@app.route("/report")
def report():
    expenses = get_all_expenses()

    chart_path = os.path.join(
        BASE_DIR,
        "static",
        "charts",
        "expenses_by_category.png"
    )

    if expenses:
        plot_expenses_by_category(expenses, chart_path)

    return render_template(
        "report.html",
        chart_file="charts/expenses_by_category.png"
    )


def run():
    app.run(debug=True)
