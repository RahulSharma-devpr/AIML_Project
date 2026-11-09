class NegativeAmountError(Exception):
    pass

def add_expense(amount):
    if amount < 0:
        raise NegativeAmountError("Amount cannot be negative")
    return amount

try:
    add_expense(-50)
except NegativeAmountError as e:
    print("Error:", e)