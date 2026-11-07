def power(base, exp=2):           
    return base ** exp

print(power(3))          #3^3
print(power(3, 4))      #3^4
print(power(exp=4, base=3))   # keyword arguments -> 3^^4

def total(*args):                  # any number of positional args (tuple)
    return sum(args)

print(total(1, 2, 3, 4))   # 10

def show(**kwargs):                # any number of keyword args (dict)
    for k, v in kwargs.items():
        print(k, "=", v)

show(name="Rahul", age=20)