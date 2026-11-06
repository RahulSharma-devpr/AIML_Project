marks = int(input("Enter your marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "Fail"

print(grade)   # C

# Ternary (one-line if)

result = "Pass" if marks >= 40 else "Fail"