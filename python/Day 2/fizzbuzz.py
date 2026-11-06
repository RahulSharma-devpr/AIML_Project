# FizzBuzz
for i in range(1, 16):
    if i % 15 == 0:
        print("multiple of 3 and 5")
    elif i % 3 == 0:
        print("multiple of 3")
    elif i % 5 == 0:
        print("multiple of 5")
    else:
        print(i)

# Prime check
n = 29
is_prime = n > 1
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        is_prime = False
        break
print(is_prime)