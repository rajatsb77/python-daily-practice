from datetime import datetime

expenses = []


def add_expense():
    category = input("Enter expense category: ")
    amount = float(input("Enter amount: ₹"))
    note = input("Enter a short note: ")

    expense = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "category": category,
        "amount": amount,
        "note": note
    }

    expenses.append(expense)
    print("Expense added successfully!")


def show_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n----- EXPENSES -----")

    total = 0

    for expense in expenses:
        print(
            f"{expense['date']} | "
            f"{expense['category']} | "
            f"₹{expense['amount']:.2f} | "
            f"{expense['note']}"
        )
        total += expense["amount"]

    print("--------------------")
    print(f"Total spent: ₹{total:.2f}")


def show_summary():
    if not expenses:
        print("No expenses recorded.")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]
        summary[category] = summary.get(category, 0) + expense["amount"]

    print("\n----- CATEGORY SUMMARY -----")

    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")


def main():
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Show Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            show_expenses()

        elif choice == "3":
            show_summary()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()