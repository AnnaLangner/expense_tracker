import tkinter as tk
from tkinter import messagebox
from datetime import date
from app.logic import add_expense


class ExpenseTrackerGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("400x300")

        # Amount
        tk.Label(root, text="Amount").pack(anchor="w", padx=10)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack(fill="x", padx=10, pady=5)

        # Category
        tk.Label(root, text="Category").pack(anchor="w", padx=10)
        self.category_entry = tk.Entry(root)
        self.category_entry.pack(fill="x", padx=10, pady=5)

        # Currency
        tk.Label(root, text="Currency").pack(anchor="w", padx=10)
        self.currency_entry = tk.Entry(root)
        self.currency_entry.insert(0, "PLN")
        self.currency_entry.pack(fill="x", padx=10, pady=5)

        # Description
        tk.Label(root, text="Description").pack(anchor="w", padx=10)
        self.description_entry = tk.Entry(root)
        self.description_entry.pack(fill="x", padx=10, pady=5)

        # Button
        tk.Button(
            root,
            text="Add Expense",
            command=self.add_expense
        ).pack(pady=15)

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

            messagebox.showinfo("Success", "Expense added successfully!")
            self.clear_fields()

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def clear_fields(self):
        self.amount_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
