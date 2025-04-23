import random

list1 = [random.randint(-100, 100) for _ in range(30)]
print(f"Generated list of 30 random numbers: {list1}")

list2 = [num for num in list1 if num > 0]
print(f"List of positive numbers: {list2}")

list3 = [num for num in list1 if num < 0]
print(f"List of negative numbers: {list3}")