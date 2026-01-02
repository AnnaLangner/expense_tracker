from dataclasses import dataclass
from datetime import date


@dataclass
class Expense:
    date: date
    amount: float
    currency: str
    category: str
    description: str
