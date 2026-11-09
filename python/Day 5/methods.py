class Circle:
    pi = 3.14159

    def __init__(self, r):
        self.r = r

    def area(self):                # instance method: uses self
        return Circle.pi * self.r ** 2

    @classmethod
    def unit(cls):                 # class method: uses cls
        return cls(1)

    @staticmethod
    def is_valid(r):               # static method: uses neither
        return r > 0

print(Circle.unit().area(), Circle.is_valid(-5))