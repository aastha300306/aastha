import random

lst = [random.randint(1, 30) for _ in range(50)]
print(f"Generated list with duplicates: {lst}")

uniquelst = list(set(lst))
print(f"List with duplicates removed: {uniquelst}")