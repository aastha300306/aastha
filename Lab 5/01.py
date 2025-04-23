import random

odd = [random.choice(range(1, 101, 2)) for _ in range(5)]
print(f"Original list of odd integers: {odd}")

even = [random.choice(range(2, 101, 2)) for _ in range(4)]
print(f"List of even integers: {even}")

odd[2] = even
print(f"List of odd integers after replacing the third element: {odd}")

flattened_list = []
for item in odd:
    if isinstance(item, list):  
        flattened_list.extend(item)
    else:
        flattened_list.append(item)
print(f"Flattened list: {flattened_list}")

flattened_list.sort()
print(f"Sorted flattened list: {flattened_list}")