list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [4, 5, 6, 8, 9]
list3 = [num for num in list1 if num not in list2]

print(f"First List: {list1}")
print(f"Second List: {list2}")
print(f"Third List (numbers in list1 but not in list2): {list3}")