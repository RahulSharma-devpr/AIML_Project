#A lambda is a small anonymous one-line function: lambda arguments: expression.
square = lambda x: x * x
add = lambda a, b: a + b
sub = lambda a, b : a - b
print(square(5), add(2, 3), sub(10, 4))  # 25 5 6

nums = [1, 2, 3, 4, 5, 6]
print(list(map(lambda x: x * 2, nums)))          # [2, 4, 6, 8, 10, 12]
print(list(filter(lambda x: x % 2 == 0, nums)))  # [2, 4, 6]

students = [("Rahul", 82), ("Asha", 91), ("Meena", 77)]
print(sorted(students, key=lambda s: s[1], reverse=True))