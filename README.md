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
│   ├── static   
│   │      └── charts
│   │            └── expenses_by_category.png
│   ├── templates
│   │      ├── add.html    
│   │      ├── expenses.html      
│   │      ├── home.html           
│   │      └── report.html  
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

### Desktop Version (GUI)

The desktop version of the application is implemented using the Tkinter library.
The interface allows users to:

* enter expense data via a form,

* display a list of expenses in a table (Treeview),

* generate a chart of expenses grouped by category.

The GUI uses the same business logic as the web version of the application.

### Web Version (Flask)

The web version of the application is built using the Flask framework.
It provides the following endpoints:

* / – home page with navigation,

* /add – expense entry form,

* /expenses – list of all expenses,

* /report – expense report and chart.

Charts are generated using the matplotlib library and saved as PNG images,
which are then displayed in the web browser.

### Analytics and Reports

The application offers basic data analytics:

* summing expenses by category,

* visualizing data in the form of bar charts.

By using the Agg backend in matplotlib, charts can be generated in a
server environment without a graphical user interface.

### Running the Application

The application can be run in two modes:

* GUI (desktop): `python main.py`

* WEB (Flask): `python main.py --web`
