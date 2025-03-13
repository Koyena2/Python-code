import json
from datetime import datetime

# File to store expense data
DATA_FILE = 'expenses.json'

# Load existing data from file
def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save data to file
def save_data(expenses):
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

# Add a new expense
def add_expense(expenses):
    try:
        date = datetime.now().strftime('%Y-%m-%d')
        amount = float(input("Enter amount spent: "))
        category = input("Enter category (e.g., food, transport, entertainment): ").strip().lower()
        description = input("Enter description: ").strip()

        expense = {
            'date': date,
            'amount': amount,
            'category': category,
            'description': description
        }

        expenses.append(expense)
        save_data(expenses)
        print("✅ Expense added successfully!")

    except ValueError:
        print("❌ Invalid input. Please enter a numeric value for the amount.")

# View all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n📊 All Expenses:")
    for idx, expense in enumerate(expenses, start=1):
        print(f"{idx}. {expense['date']} - {expense['category'].title()}: ${expense['amount']:.2f} ({expense['description']})")

# Generate monthly summary
def monthly_summary(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    summary = {}
    for expense in expenses:
        month = expense['date'][:7]  # YYYY-MM format
        summary[month] = summary.get(month, 0) + expense['amount']

    print("\n📅 Monthly Summary:")
    for month, total in summary.items():
        print(f"{month}: ${total:.2f}")

# Generate category-wise summary
def category_summary(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    summary = {}
    for expense in expenses:
        category = expense['category']
        summary[category] = summary.get(category, 0) + expense['amount']

    print("\n📂 Category-wise Summary:")
    for category, total in summary.items():
        print(f"{category.title()}: ${total:.2f}")

# User interface
def main():
    expenses = load_data()
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Category-wise Summary")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            monthly_summary(expenses)
        elif choice == '4':
            category_summary(expenses)
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
