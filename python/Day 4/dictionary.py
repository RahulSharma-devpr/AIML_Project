student = {"name": "Sharma", "age": 21, "course": "Python"}

print(student["name"])
print(student.get("grade", "N/A"))   # safe access with default
student["age"] = 22                   # update
student["city"] = "Delhi"             # add
del student["course"]                 # delete

for key, value in student.items():
    print(key, ":", value)

# Dictionary comprehension
cubes = {x: x ** 3 for x in range(1, 5)}   # {1: 1, 2: 8, 3: 27, 4: 64}

# Count frequency (very common pattern)
text = "banana"
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)    # {'b': 1, 'a': 3, 'n': 2}