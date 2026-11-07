#defining and calling func.
name = input("Enter your name: ")
def greet(name):
    return f"Hello, {name}!"

print(greet(f"{name}"))