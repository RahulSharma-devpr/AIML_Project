
n=int(input("Enter a number: "))
def factorial(n):
    if n <= 1:            
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

print(factorial(n))                     
print([fibonacci(i) for i in range(8)])  
print(sum_digits(1234))                  