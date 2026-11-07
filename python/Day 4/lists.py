list = ["apple", "banana", "c herry"]

list.append("mango")         # add at end
list.insert(1, "kiwi")       # add at index
list.remove("banana")        # remove by value
last = list.pop()            # remove and return last
list.sort()                  # sort in place
print(list, last)
nums = [5, 2, 9, 1, 7]
print(nums[1:4], nums[::-1])   # slicing, reverse
print(len(nums), sum(nums), max(nums), min(nums))

# List comprehension
squares = [x ** 2 for x in range(1, 6)]            # [1, 4, 9, 16, 25]
evens = [x for x in range(1, 21) if x % 2 == 0]
print(squares, evens)