import tkinter as tk
from tkinter import messagebox
from datetime import date
from tkinter.ttk import Treeview
from app.logic import add_expense, get_all_expenses
from app.analytics import plot_expenses_by_category


class ExpenseTrackerGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("800x500")

        # FORM FRAME
        form_frame = tk.LabelFrame(root, text="Add Expense")
        form_frame.pack(fill="x", padx=10, pady=5)

        # Amount
        tk.Label(form_frame, text="Amount").grid(row=0, column=0, padx=5, pady=5)
        self.amount_entry = tk.Entry(form_frame)
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5)

        # Category
        tk.Label(form_frame, text="Category").grid(row=0, column=2, padx=5, pady=5)
        self.category_entry = tk.Entry(form_frame)
        self.category_entry.grid(row=0, column=3, padx=5, pady=5)

        # Currency
        tk.Label(form_frame, text="Currency").grid(row=1, column=0, padx=5, pady=5)
        self.currency_entry = tk.Entry(form_frame)
        self.currency_entry.insert(0, "PLN")
        self.currency_entry.grid(row=1, column=1, padx=5, pady=5)

        # Description
        tk.Label(form_frame, text="Description").grid(row=1, column=2, padx=5, pady=5)
        self.description_entry = tk.Entry(form_frame)
        self.description_entry.grid(row=1, column=3, padx=5, pady=5)

        # Button
        tk.Button(
            form_frame,
            text="Add Expense",
            command=self.add_expense
        ).grid(row=2, column=0, columnspan=4, pady=10)

        # LIST FRAME
        list_frame = tk.LabelFrame(root, text="Expenses")
        list_frame.pack(fill="both", expand=True, padx=10, pady=5)

        columns = ("date", "amount", "currency", "category", "description")
        self.tree = Treeview(list_frame, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, anchor="center")

        self.tree.pack(fill="both", expand=True)

        # BUTTONS FRAME
        buttons_frame = tk.Frame(root)
        buttons_frame.pack(pady=5)

        tk.Button(
            buttons_frame,
            text="Refresh list",
            command=self.load_expenses
        ).pack(side="left", padx=5)

        tk.Button(
            buttons_frame,
            text="Show chart",
            command=self.show_chart
        ).pack(side="left", padx=5)

        self.load_expenses()

    def add_expense(self):
        try:
            amount = float(self.amount_entry.get())
            category = self.category_entry.get()
            currency = self.currency_entry.get()
            description = self.description_entry.get()

            add_expense(
                expense_date=date.today(),
                amount=amount,
                currency=currency,
                category=category,
                description=description
            )

            self.clear_fields()
            self.load_expenses()
            messagebox.showinfo("Success", "Expense added successfully!")

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def clear_fields(self):
        self.amount_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)

    def load_expenses(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        expenses = get_all_expenses()
        for e in expenses:
            self.tree.insert(
                "",
                "end",
                values=(
                    e.date.isoformat(),
                    e.amount,
                    e.currency,
                    e.category,
                    e.description
                )
            )

    def show_chart(self):
        expenses = get_all_expenses()
        if not expenses:
            messagebox.showwarning("No data", "No expenses to display")
            return

        plot_expenses_by_category(expenses)