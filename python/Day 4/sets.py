colors = {"red", "green", "blue"}
colors.add("yellow")
colors.discard("red")

print(set([1, 2, 2, 3, 3, 3]))     # {1, 2, 3}  (removes duplicates)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)    # union        {1, 2, 3, 4, 5, 6}
print(a & b)    # intersection {3, 4}
print(a - b)    # difference   {1, 2}
print(a ^ b)    # symmetric difference {1, 2, 5, 6}