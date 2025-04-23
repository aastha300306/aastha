def reverse_list_recursive(lst):
    if len(lst) == 0:  
        return []
    return [lst[-1]] + reverse_list_recursive(lst[:-1]) 

numbers = [1, 2, 3, 4, 5]
reversed_numbers = reverse_list_recursive(numbers)
print("Original List:", numbers)
print("Reversed List:", reversed_numbers)