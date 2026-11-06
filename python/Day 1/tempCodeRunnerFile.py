bill = float(input("Enter the total bill amount: "))
people = int(input("Enter the number of people: "))
tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))

tip_amount = bill * (tip_percentage / 100)
total_amount = bill + tip_amount
per_person_amount = total_amount / people

print("\n----- RECEIPT -----")
print(f"Bill      : {bill:.2f}")
print(f"Tip       : {tip_amount:.2f}")
print(f"Total     : {total_amount:.2f}")
print(f"Per person: {per_person_amount:.2f}")