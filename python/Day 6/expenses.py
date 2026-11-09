import json
import os

FILE = "expenses.json"

class InvalidAmountError(Exception):
    pass

def load_expenses():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE) as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("File was corrupted, starting fresh")
        return []

def save_expenses(expenses):
    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=2)

def add_expense(expenses, category, amount):
    if amount <= 0:
        raise InvalidAmountError("Amount must be positive")
    expenses.append({"category": category, "amount": amount})

def summary(expenses):
    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    return totals

expenses = load_expenses()

while True:
    print("\n1. Add expense   2. Summary   3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        try:
            category = input("Category: ").strip().lower()
            amount = float(input("Amount: "))
            add_expense(expenses, category, amount)
            save_expenses(expenses)
            print("Saved!")
        except ValueError:
            print("Amount must be a number")
        except InvalidAmountError as e:
            print("Error:", e)
    elif choice == "2":
        totals = summary(expenses)
        for cat, total in totals.items():
            print(f"{cat:<12}{total:.2f}")
        print("Total:", sum(totals.values()))
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")