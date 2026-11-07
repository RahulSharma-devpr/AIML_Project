def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

def average(*nums):
    return sum(nums) / len(nums)

operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else "Cannot divide by zero",
}

def calculate(a, b, op):
    if op in operations:
        return operations[op](a, b)
    return "Invalid operator"

while True:
    print("\n1. Basic calculation\n2. Factorial\n3. Average\n4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        a = float(input("First number: "))
        b = float(input("Second number: "))
        op = input("Operator (+ - * /): ")
        print("Result:", calculate(a, b, op))
    elif choice == "2":
        print("Result:", factorial(int(input("Number: "))))
    elif choice == "3":
        nums = list(map(float, input("Numbers separated by space: ").split()))
        print("Average:", average(*nums))
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")