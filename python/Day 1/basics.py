
# variable And Datatypes , string , float , intetger , boolean , NoneType
name = "Rahul"        # str
age = 21             # int
height = 5.6         # float
is_student = True    # bool
nothing = None       # NoneType

print(type(name), type(age), type(height), type(is_student), type(nothing))


#Type conversion and input
#input() always returns a string, so convert it when you need a number.

x = int("10")        # 10
y = float("3.5")     # 3.5
z = str(100)         # "100"
print(bool(), bool(""), bool("false"))   # False False True
print(type(x), type(y), type(z))

#Strings and f-strings
name = "Rahul"
age = 21
s = "Python Revision"
print(s.upper(), s.lower(), len(s))
print(s[0], s[-6], s[0:6])      # P n Python
print(s.replace("Python", "Java"))
print(f"{name} is {age} {s}  years old")

#Operators
a, b = 17, 5

# Arithmetic
print(a + b, a - b, a * b, a / b)   # 22 12 85 3.4
print(a // b, a % b, a ** b)        # 3 2 1419857

# Comparison
print(a > b, a == b, a != b)

# Logical
print(a > 10 and b < 10, a > 20 or b < 10, not (a > b))

# Assignment
a += 3     # a = a + 3

# Membership and identity
print("Py" in "Python")   # True
print(a is b)             # False