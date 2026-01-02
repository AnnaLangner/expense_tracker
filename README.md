# Expense Tracker

An expense tracking app with features like adding, editing, filtering, reporting, charting, exporting, multi-currency support, and basic analytics.

## Basic Features (MVP)

* Adding an expense

* Displaying a list of expenses

* Saving/Reading data (JSON)

* Date, amount, category, currency, description

### Expense structure

```
{
    "date": "2026-01-02",
    "amount": 50.0,
    "currency": "PLN",
    "category": "Food",
    "description": "Lunch"
}
```
### Project structure

```
expense_tracker/
│
├── app/
│   ├── __init__.py
│   ├── models.py    
│   ├── storage.py     
│   ├── logic.py        
│   ├── analytics.py    
│   ├── reports.py      
│   ├── gui.py           
│   └── web.py           
│
├── data/
│   └── expenses.json
│
├── tests/
│   └── test_logic.py
│
├── main.py
├── requirements.txt
└── README.md

```