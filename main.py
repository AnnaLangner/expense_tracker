import sys
import tkinter as tk
from app.web import run as run_web
from app.gui import ExpenseTrackerGUI


def run_gui():
    root = tk.Tk()
    app = ExpenseTrackerGUI(root)
    root.mainloop()


def main():
    if "--web" in sys.argv:
        run_web()
    else:
        run_gui()


if __name__ == "__main__":
    main()
