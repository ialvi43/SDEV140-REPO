import tkinter as tk
from tkinter import ttk, messagebox

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        self.expenses = []

        # Labels and Entry widgets for expense input
        tk.Label(root, text="Expense:").grid(row=0, column=0, padx=5, pady=5)
        self.expense_entry = tk.Entry(root)
        self.expense_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(root, text="Amount:").grid(row=1, column=0, padx=5, pady=5)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=1, column=1, padx=5, pady=5)

        # Button to add expense
        self.add_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        # Button to show expenses with pie chart
        self.show_button = tk.Button(root, text="Show Expenses", command=self.show_expenses)
        self.show_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

    def add_expense(self):
        expense = self.expense_entry.get()
        amount = self.amount_entry.get()
        if expense and amount:
            try:
                amount = float(amount)
                self.expenses.append((expense, amount))
                self.expense_entry.delete(0, tk.END)
                self.amount_entry.delete(0, tk.END)
                messagebox.showinfo("Success", "Expense added successfully!")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid amount.")
        else:
            messagebox.showerror("Error", "Please enter both expense and amount.")

    def show_expenses(self):
        # Calculate total amount
        total = sum(expense[1] for expense in self.expenses)
        
        # Create a new window for displaying expenses
        new_window = tk.Toplevel(self.root)
        new_window.title("Expenses")

        # Create a Progressbar to simulate a pie chart
        pb = ttk.Progressbar(new_window, orient='horizontal', length=300, mode='determinate', maximum=total)
        pb.grid(row=0, column=0, padx=5, pady=5)

        # Add expenses as segments to the Progressbar
        current_value = 0
        for expense in self.expenses:
            expense_name, expense_amount = expense
            pb['value'] = current_value
            pb.update_idletasks()  # Update the Progressbar
            pb['value'] += expense_amount
            current_value += expense_amount

            # Add a label to display the expense name and amount
            tk.Label(new_window, text=f"{expense_name}: ${expense_amount:.2f}").grid(sticky='w')

        pb['value'] = total  # Set value to total to ensure it reaches 100%
        pb.update_idletasks()  # Update the Progressbar

        # Add a label to display the total amount
        tk.Label(new_window, text=f"Total: ${total:.2f}").grid(sticky='w')


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()

