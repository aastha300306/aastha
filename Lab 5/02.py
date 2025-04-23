import random

lst = [random.randint(1, 100) for _ in range(20)]
print(f"Generated list of random integers: {lst}")

a = int(input("Enter a number to search for in the list: "))

positions = [index for index, value in enumerate(lst) if value == a]

if positions:
    print(f"The number {a} is found at the following positions: {positions}")
else:
    print(f"The number {a} is not found in the list.")