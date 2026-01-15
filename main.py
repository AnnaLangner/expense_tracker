import tkinter as tk
from app.gui import ExpenseTrackerGUI


def main():
    root = tk.Tk()
    app = ExpenseTrackerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()