
def min_max(nums):
    return min(nums), max(nums)    # returns a tuple

low, high = min_max([4, 9, 1, 7])

x = 10                 # global
def change():
    x = 5              # local, does not change the global x
    return x