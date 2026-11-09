try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("No errors happened")      # runs only if try succeeded
finally:
    print("Always runs")             # cleanup code