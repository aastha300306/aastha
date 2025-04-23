def sanitize_list(lst):
    if not lst:  
        return []
    first = 0 if lst[0] < 0 else lst[0]
    return [first] + sanitize_list(lst[1:])

example_list = [-5, 3, -2, 7, -1, 0, 4]
sanitized_list = sanitize_list(example_list)
print("Sanitized List:", sanitized_list)