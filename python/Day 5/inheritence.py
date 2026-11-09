class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)     # reuse parent's __init__
        self.breed = breed

    def speak(self):               # overriding
        return f"{self.name} says Woof"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow"

for pet in [Dog("Rex", "Labrador"), Cat("Mimi")]:
    print(pet.speak())             # polymorphism

print(isinstance(Dog("Rex", "Lab"), Animal))   # True