students = {}   # name -> list of marks

def add_student(name, marks):
    students[name] = marks

def average(marks):
    return sum(marks) / len(marks)

def topper():
    name = max(students, key=lambda n: average(students[n]))
    return name, average(students[name])      # returns a tuple

def show_report():
    print(f"\n{'Name':<10}{'Average':<10}{'Grade'}")
    for name, marks in students.items():
        avg = average(marks)
        grade = "A" if avg >= 85 else "B" if avg >= 70 else "C"
        print(f"{name:<10}{avg:<10.2f}{grade}")

add_student("Asha", [90, 85, 92])
add_student("Ravi", [70, 65, 80])
add_student("Meena", [88, 91, 79])

show_report()

top_name, top_avg = topper()
print(f"\nTopper: {top_name} ({top_avg:.2f})")

all_marks = [m for marks in students.values() for m in marks]
print("Unique marks:", sorted(set(all_marks)))
print("Highest mark:", max(all_marks))
print("Students above 80 avg:", [n for n, m in students.items() if average(m) > 80])