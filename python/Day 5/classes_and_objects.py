class Student:
    school = "ABC School"          # class attribute (shared by all objects)

    def __init__(self, name, age):
        self.name = name           # instance attributes (unique per object)
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old."

    def __str__(self):             # what print(obj) shows
        return f"Student({self.name}, {self.age})"

s1 = Student("XYZ", 21)
s2 = Student("ABC", 20)
print(s1.introduce())
print(s2, Student.school)
